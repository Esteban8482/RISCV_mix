import sys

class Automaton:
    def __init__(self, states, alphabet, s0, trans, accept):
        self.states = states
        self.alphabet = alphabet
        self.s0 = s0
        self.trans = trans
        self.accept = accept

    def accepts(self, input):
        s = self.s0
        for c in input:
            s = self.trans[s][c]
        return s in self.accept

def fileToString(filename):
    with open(filename, 'r') as f:
        data = f.read()
        return data


a = Automaton(["q1", "q2", "q3"],
              ['0', '1'],
              "q1",
              {"q1": {'0': "q1", '1': "q2"},
               "q2": {'0': "q3", '1': "q2"},
               "q3": {'0': "q2", '1': "q2"}},
              ["q2"])

integers = Automaton(["q0", "q1", "q2", "q3"],
                     ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-", "+"],
                     "q0",
                     {"q0":{"0": "q2", "1": "q2", "2": "q2", "3": "q2", "4": "q2", "5": "q2", "6": "q2", "7": "q2", "8": "q2", "9": "q2", "-": "q1", "+": "q1"},
                      "q1":{"0": "q1", "1": "q2", "2": "q2", "3": "q2", "4": "q2", "5": "q2", "6": "q2", "7": "q2", "8": "q2", "9": "q2", "-": "q3", "+": "q3"},
                      "q2":{"0": "q2", "1": "q2", "2": "q2", "3": "q2", "4": "q2", "5": "q2", "6": "q2", "7": "q2", "8": "q2", "9": "q2", "-": "q3", "+": "q3"},
                      "q3":{"0": "q3", "1": "q3", "2": "q3", "3": "q3", "4": "q3", "5": "q3", "6": "q3", "7": "q3", "8": "q3", "9": "q3", "-": "q3", "+": "q3"}},
                      ["q2"])


# x = a.accepts("00")
# print(x)
# print(integers.accepts("01"))
# print(integers.accepts("+16543"))
# print(integers.accepts("-16543"))
# print(integers.accepts("-165-43"))
# print(integers.accepts("-165+--43"))

# print(sys.argv[1])
s = fileToString(sys.argv[1])
print(s.split())
