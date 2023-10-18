#include "KaleidoscopeLexer.h"
#include "KaleidoscopeParser.h"
#include "MIPSASMcodegen.hh"
#include "antlr4-runtime.h"
#include <fstream>
#include <iostream>
#include <string>

using namespace antlr4;
using namespace std;
using namespace Kaleidoscope;

int main(int argc, const char **argv) {

  if (argc != 3) {
    cerr << "Expecting exactly one argument. Example: " << endl
         << "./kalc source.kl outut.mips" << endl;
    return 1;
  }

  string sourceCode(argv[1]);
  string outputCode(argv[2]);

  ifstream sc(sourceCode);
  if (!sc) {
    cerr << "Error openning the file: " << sourceCode << endl;
    return 1;
  }

  ANTLRInputStream input(sc);
  KaleidoscopeLexer lexer(&input);
  CommonTokenStream tokens(&lexer);

  tokens.fill();

  KaleidoscopeParser parser(&tokens);
  tree::ParseTree *tree = parser.program();

  // Semantic analysis

  // Code generation
  ofstream output(outputCode);
  MIPSCodeEmitter ce(output);
  MIPSAsmGenerator v(ce, false);
  v.visit(tree);
  return 0;
}