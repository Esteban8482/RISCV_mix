
class Visitor(object):
    def visit(self, tree):
        method = getattr(self, tree.head, None)
        #print("Visit for {} will call {}".format(tree.head, method))
        if method:
            method(tree)

    def start(self, tree):
        #print("Start*- {}".format(tree))
        program = tree.tail[0]
        self.visit(program)

    def program(self, tree):
        #print("Program*- {}".format(tree))
        for funcdef in tree.tail[:-1]:
            self.visit(funcdef)
        main = tree.tail[-1]
        self.visit(main)

    def functiondef(self, tree):
        functionName = tree.tail[1]
        #print("Functiondef*- {} -* {}".format(functionName,tree))
        i = 3
        while tree.tail[i] != ')':
            #print("Argument {}".format(tree.tail[i]))
            i = i + 1
        i = i + 2
        body = tree.tail[i]
        #print("Body {}".format(body))
        self.visit(body)

    def conditional(self, tree):
        #print("Conditional*- {}".format(tree))
        guard = tree.tail[2]
        self.visit(guard)
        thenExp = tree.tail[5]
        self.visit(thenExp)
        elseExp = tree.tail[9]
        self.visit(elseExp)

    def functioncall(self, tree):
        fname = tree.tail[0]
        #print("Functioncall*- {} -* {}".format(fname, tree))
        args = tree.tail[2:-1]
        arity = len(args)
        for exp in args:
            self.visit(exp)


    def logicalexpression(self, tree):
        #print("Logical expression*- {}".format(tree))
        leftExp = tree.tail[0]
        self.visit(leftExp)
        rightExp = tree.tail[2]
        self.visit(rightExp)
        rel = tree.tail[1]

    def variable(self, tree):
        name = tree.tail[0]
        #print("Variable*- {}".format(name))

    def number(self, tree):
        value = tree.tail[0]
        #print("Number*- {}".format(value))

    def addexpr(self, tree):
        #print("Addexpr *- {}".format(tree))
        leftExp = tree.tail[0]
        self.visit(leftExp)
        rightExp = tree.tail[2]
        self.visit(rightExp)
        op = tree.tail[1]

    def mulexpr(self, tree):
        #print("Mulexpr *- {}".format(tree))
        leftExp = tree.tail[0]
        self.visit(leftExp)
        rightExp = tree.tail[2]
        self.visit(rightExp)
        op = tree.tail[1]
