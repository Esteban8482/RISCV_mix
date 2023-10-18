class CodeGenerator(object):
    def __init__(self, codeEmitter, useSpim):
        # The code emitter for the instructions
        self.ce = codeEmitter
        # Counter to generate unique labels for the conditionals
        self.condCounter = 0
        # Positions for the arguments of the defined functions
        self.functionArguments = {}
        # Current function name being processed
        self.currFunctionDef = ""
        # Whether to generate helper code to use spim on the generated code
        self.useSpim = useSpim



    ####################
    ## Helper methods ##
    ####################
    
    # Push the value of register @reg on the stack.
    # Invariant: sp stores the address of the first unused top
    #            of the stack 
    def pushRegister(self, reg):
        self.ce.sw(reg, "sp")
        self.ce.addiu("sp", "sp", -4)
    # Pop the stack and leave the top in @reg
    # Invariant: sp stores the address of the first unused top
    #            of the stack 
    def popInRegister(self, reg):
        self.ce.lw(reg, "sp", 4)
        self.ce.addiu("sp", "sp", 4)

    ##################################################
    ## Methods to visit the AST for code generation ##
    ##################################################
    def visit(self, tree):
        method = getattr(self, tree.head, None)
        # print("Visit for {} will call {}".format(tree.head, method))
        if method:
            return method(tree)
        else:
            print("Method {} is not defined by the class".format(method))

    def start(self, tree):
        # self.ce.raw("Code generated")
        #print("Start*- {}".format(tree))
        program = tree.tail[0]
        self.visit(program)

    def program(self, tree):
        #print("Program*- {}".format(tree))
        if self.useSpim:
            self.dataHeader()

        for funcdef in tree.tail[:-1]:
            self.visit(funcdef)
        main = tree.tail[-1]

        self.ce.newLabel("main")
        self.visit(main)

        if self.useSpim:
            self.exit()

    def functiondef(self, tree):
        functionName = tree.tail[1]
        self.ce.newLabel(functionName)
        self.ce.move("fp", "sp")
        self.pushRegister("ra")
        #print("Functiondef*- {} -* {}".format(functionName,tree))
        arguments = {}
        i = 3
        a = 0
        while tree.tail[i] != ')':
            if tree.tail[i] != ',':
                arg = tree.tail[i]
                argPos = a
                arguments[arg] = argPos
                a = a + 1
            i = i + 1
        self.functionArguments[functionName] = arguments
        self.currFunctionDef = functionName
        # print(self.functionArguments)
        i = i + 2
        body = tree.tail[i]
        self.visit(body)
        # Complete the activation record
        self.ce.lw("ra", "sp", 4)
        self.ce.addiu("sp", "sp", 12) # Needs to remove 12 and put a number of bytes proportional to the number of params
        self.ce.lw("fp", "sp")
        self.ce.jr("ra")

    def functioncall(self, tree):
        fname = tree.tail[0]
        self.pushRegister("fp")
        # print("Functioncall*- {} -* {}".format(fname, tree))
        args = [x for x in tree.tail[2:-1] if x != ',']
        arity = len(args)
        for exp in args:
            self.visit(exp)
            self.pushRegister("a0")
        self.ce.jal(fname)

    def conditional(self, tree):
        #print("Conditional*- {}".format(tree))
        guard = tree.tail[2]
        condId = self.visit(guard)
        
        trueLabel = "true_" + str(condId)
        falseLabel = "false_" + str(condId)
        exitLabel = "exit_" + str(condId)

        thenExp = tree.tail[5]
        elseExp = tree.tail[9]
        
        self.ce.newLabel(falseLabel)
        self.visit(elseExp)
        self.ce.b(exitLabel)

        self.ce.newLabel(trueLabel)
        self.visit(thenExp)
        self.ce.newLabel(exitLabel)


    def logicalexpression(self, tree):
        #print("Logical expression*- {}".format(tree))
        leftExp = tree.tail[0]
        self.visit(leftExp)
        self.pushRegister("a0")
        rightExp = tree.tail[2]
        self.visit(rightExp)
        self.popInRegister("t1")

        condId = self.condCounter
        self.condCounter = self.condCounter + 1
        jLabel = "true_" + str(condId)

        rel = tree.tail[1]
        if rel == "<":
            self.ce.blt("t1", "a0", jLabel)
        elif rel == ">":
            self.ce.bgt("t1", "a0", jLabel)
        elif rel == "<=":
            self.ce.ble("t1", "a0", jLabel)
        elif rel == ">=":
            self.ce.bge("t1", "a0", jLabel)
        elif rel == "==":
            self.ce.beq("t1", "a0", jLabel)
        else:
            assert rel == "!="
            self.ce.bne("t1", "a0", jLabel)

        return condId

    def variable(self, tree):
        name = tree.tail[0]
        pos = self.functionArguments[self.currFunctionDef][name]
        offset = (pos + 1) * 4
        self.ce.lw("a0", "fp", offset)
        #print("Variable*- {}".format(name))

    def number(self, tree):
        value = tree.tail[0]
        # Must assert that the number fits in a 32 bits integer
        self.ce.li("a0", value)
        #print("Number*- {}".format(value))

    def addexpr(self, tree):
        # print("Addexpr *- {}".format(tree))
        leftExp = tree.tail[0]
        self.visit(leftExp)
        self.pushRegister("a0")

        rightExp = tree.tail[2]
        self.visit(rightExp)

        self.popInRegister("t1")

        op = tree.tail[1]
        if op == "+":
            self.ce.add("a0", "t1", "a0")
        else:
            self.ce.sub("a0", "t1", "a0")


    def mulexpr(self, tree):
        #print("Mulexpr *- {}".format(tree))
        leftExp = tree.tail[0]
        self.visit(leftExp)
        self.pushRegister("a0")

        rightExp = tree.tail[2]
        self.visit(rightExp)

        self.popInRegister("t1")

        op = tree.tail[1]
        if op == "*":
            self.ce.mul("a0", "t1")
            self.ce.mflo("a0")
        elif op == "/":
            self.ce.div("t1", "a0")
            self.ce.mflo("a0")
        else:
            assert op == "%"
            self.ce.div("t1", "a0")
            self.ce.mfhi("a0")

    def parexpression(self, tree):
        #print("Parexpr *- {}".format(tree))
        self.visit(tree.tail[1])

    #############################
    ## Helper code to use spim ##
    #############################
    def dataHeader(self):
        ce = self.ce
        ce.raw(".data");
        ce.raw("exit_msg: .asciiz \"Program finished:\\n\"")
        ce.raw("newline: .asciiz \"\\n\"")
        ce.raw(".text")
        ce.raw(".globl main")

    def exit(self):
        ce = self.ce
        ce.raw("\n\nexit:")
        self.pushRegister("a0")
        ce.raw("\t# Print message")
        ce.raw("\tli  $v0, 4")
        ce.raw("\tla  $a0, exit_msg")
        ce.raw("\tsyscall")
        ce.raw("\t# Restore the result of the program which is on the stack")
        self.popInRegister("a0")
        ce.raw("\tli  $v0, 1")
        ce.raw("\tsyscall")
        ce.raw("\t# Print one last new line")
        ce.raw("\tli $v0, 4")
        ce.raw("\tla $a0, newline")
        ce.raw("\tsyscall")
        ce.raw("\t# Exit the program")
        ce.raw("\tli $v0, 10")
        ce.raw("\tsyscall")
