#ifndef __CODE_EMITTER__
#define __CODE_EMITTER__

#include <fstream>
#include <string>
#include <unordered_map>

using namespace std;

class MIPSCodeEmitter {
private:
  /**
   * Stream where the code is emitted.
   */
  ofstream &os;
  /**
   * Associates abstract registers with particular register names of the
   * hardware.
   */
  unordered_map<string, string> reg;

  string sp; ///> Stores the stack pointer.
  string fp; ///> Stores the frame pointer.
  string a0; ///> Accumulator register.
  string t1; ///> Temporary register.
  string ra; ///> Return address.

public:
  MIPSCodeEmitter(ofstream &s)
      : os(s), sp("$sp"), fp("$fp"), a0("$a0"), t1("$t1"), ra("$ra") {
    reg[sp] = "$sp";
    reg[fp] = "$fp";
    reg[a0] = "$a0";
    reg[t1] = "$t1";
    reg[ra] = "$ra";
  }
  /**
   * Load inmmediate operation.
   * @param r   Register name
   * @param val Value to load (constant)
   */
  void li(const string &r, int val) {
    os << "li " << reg[r] << ", " << val << endl;
  }
  /**
   * Load word from memmory
   * @param r1     Target register
   * @param r2     Register with the address
   * @param offset Offset for the address to read
   */
  void lw(const string &r1, const string &r2, int offset = 0) {
    os << "lw " << reg[r1] << ", " << offset << "(" << reg[r2] << ")" << endl;
  }
  void move(const string &r1, const string &r2) {
    os << "add " << reg[r1] << ", $zero, " << reg[r2] << endl;
  }
  void sw(const string &r1, const string &r2, int offset = 0) {
    os << "sw " << reg[r1] << ", " << offset << "(" << reg[r2] << ")" << endl;
  }
  void addiu(const string &r1, const string &r2, int imm) {
    os << "addiu " << reg[r1] << ", " << reg[r2] << ", " << imm << endl;
  }
  void add(const string &r1, const string &r2, const string &r3) {
    os << "add " << reg[r1] << ", " << reg[r2] << ", " << reg[r3] << endl;
  }
  void sub(const string &r1, const string &r2, const string &r3) {
    os << "sub " << reg[r1] << ", " << reg[r2] << ", " << reg[r3] << endl;
  }
  void mult(const string &r1, const string &r2) {
    os << "mult " << reg[r1] << ", " << reg[r2] << endl;
  }
  void div(const string &r1, const string &r2) {
    os << "div " << reg[r1] << ", " << reg[r2] << endl;
  }
  void mflo(const string &r1) { os << "mflo " << reg[r1] << endl; }
  void mfhi(const string &r1) { os << "mfhi " << reg[r1] << endl; }
  void beq(const string &r1, const string &r2, const string &label) {
    os << "beq " << reg[r1] << ", " << reg[r2] << ", " << label << endl;
  }
  void blt(const string &r1, const string &r2, const string &label) {
    os << "blt " << reg[r1] << ", " << reg[r2] << ", " << label << endl;
  }
  void bgt(const string &r1, const string &r2, const string &label) {
    os << "bgt " << reg[r1] << ", " << reg[r2] << ", " << label << endl;
  }
  void ble(const string &r1, const string &r2, const string &label) {
    os << "ble " << reg[r1] << ", " << reg[r2] << ", " << label << endl;
  }
  void bge(const string &r1, const string &r2, const string &label) {
    os << "bge " << reg[r1] << ", " << reg[r2] << ", " << label << endl;
  }
  void bne(const string &r1, const string &r2, const string &label) {
    os << "bne " << reg[r1] << ", " << reg[r2] << ", " << label << endl;
  }
  /**
   * Unconditional branch
   * @param label name of the label to jump to.
   */
  void b(const string &label) { os << "b " << label << endl; }
  void jal(const string &label) { os << "jal " << label << endl; }
  void jr(const string &r1) { os << "jr " << reg[r1] << endl; }
  /**
   * Creates a new label. A label is a place to jump to.
   * @param label name of the label.
   */
  void newLabel(const string &label) { os << label << ":" << endl; }
  /**
   * Raw output for arbitrary code.
   * @param inst code to generate.
   */
  void raw(const string &inst) { os << inst << endl; }
  /**
   * Outputs a comment
   */
  void comment(const string &c) { os << "\t# " << c << endl; }
};

#endif