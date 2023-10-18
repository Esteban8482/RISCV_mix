
# This class implements a code emitter for the MIPS instruction set.
# As the register names become difficult we follow the conventions 
# and the names used in:
# http://www.mrc.uidaho.edu/mrc/people/jff/digital/MIPSir.html
class MIPSCodeEmitter(object):
    def __init__(self, file):
        self.file = file
        self.registers = {
            "a0": "$a0", # Accumulator register
            "sp": "$sp", # Stack pointer
            "fp": "$fp", # Frame pointer
            "t1": "$t1", # Temporal register 1
            "ra": "$ra", # Return address
        }

    def println(self, str):
        print(str, file=self.file)

    def raw(self, str):
        self.println(str)

    def sw(self, t, s, offset = None):
        if offset is None:
            offset = 0
        regs = self.registers
        self.println("sw {}, {}({})".format(regs[t], offset, regs[s]))

    def lw(self, t, s, offset = None):
        if offset is None:
            offset = 0
        regs = self.registers
        self.println("lw {}, {}({})".format(regs[t], offset, regs[s]))

    def li(self, t, imm):
        regs = self.registers
        self.println("li {}, {}".format(regs[t], imm))

    def addiu(self, t, s, imm):
        regs = self.registers
        self.println("addiu {}, {}, {}".format(regs[t], regs[s], imm))

    def newLabel(self, label):
        self.println("{}:".format(label))

    def move(self, dst, src):
        regs = self.registers
        self.println("add {}, $zero, {}".format(regs[dst], regs[src]))

    def jr(self, s):
        regs = self.registers
        self.println("jr {}".format(regs[s]))

    def jal(self, label):
        self.println("jal {}".format(label))

    def blt(self, r, s, label):
        regs = self.registers
        self.println("blt {}, {}, {}".format(regs[r], regs[s], label))

    def bgt(self, r, s, label):
        regs = self.registers
        self.println("bgt {}, {}, {}".format(regs[r], regs[s], label))

    def ble(self, r, s, label):
        regs = self.registers
        self.println("ble {}, {}, {}".format(regs[r], regs[s], label))

    def bge(self, r, s, label):
        regs = self.registers
        self.println("bge {}, {}, {}".format(regs[r], regs[s], label))

    def beq(self, r, s, label):
        regs = self.registers
        self.println("beq {}, {}, {}".format(regs[r], regs[s], label))

    def bne(self, r, s, label):
        regs = self.registers
        self.println("bne {}, {}, {}".format(regs[r], regs[s], label))

    def b(self, label):
        self.println("b {}".format(label))

    def add(self, d, s, t):
        regs = self.registers
        self.println("add {}, {}, {}".format(regs[d], regs[s], regs[t]))

    def sub(self, d, s, t):
        regs = self.registers
        self.println("sub {}, {}, {}".format(regs[d], regs[s], regs[t]))

    def mul(self, d, s):
        regs = self.registers
        self.println("mult {}, {}".format(regs[d], regs[s]))
    
    def div(self, d, s):
        regs = self.registers
        self.println("div {}, {}".format(regs[d], regs[s]))

    def mflo(self, d):
        regs = self.registers
        self.println("mflo {}".format(regs[d]))

    def mfhi(self, d):
        regs = self.registers
        self.println("mfhi {}".format(regs[d]))

