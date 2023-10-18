#include <fstream>
#include <iostream>
#include <keystone/keystone.h>
#include <string>

using namespace std;

int test_ks(ks_arch arch, int mode, const char *assembly, int syntax) {
  ks_engine *ks;
  ks_err err;
  size_t count;
  unsigned char *encode;
  size_t size;

  err = ks_open(arch, mode, &ks);
  if (err != KS_ERR_OK) {
    printf("ERROR: failed on ks_open(), quit\n");
    return -1;
  }
  //
  if (syntax)
    ks_option(ks, KS_OPT_SYNTAX, syntax);

  if (ks_asm(ks, assembly, 0, &encode, &size, &count)) {
    printf("ERROR: failed on ks_asm() with count = %lu, error code = %u\n",
           count, ks_errno(ks));
  } else {
    size_t i;

    // printf("%s = ", assembly);
    for (i = 0; i < size; i++) {
      printf("%02x ", encode[i]);
    }
    printf("\n");
    printf("Assembled: %lu bytes, %lu statements\n\n", size, count);
  }

  // NOTE: free encode after usage to avoid leaking memory
  ks_free(encode);

  // close Keystone instance when done
  ks_close(ks);

  return 0;
}

int main(int argc, char **argv) {
  if (argc != 2) {
    cerr << "Must be called: ./" << argv[0] << " source.asm" << endl;
    return 1;
  }
  string fileName(argv[1]);
  ifstream ifs(fileName);
  string code((istreambuf_iterator<char>(ifs)), (istreambuf_iterator<char>()));
  // cout << code << endl;
  test_ks(KS_ARCH_MIPS, KS_MODE_MIPS32, code.c_str(), 0);
  return 0;
}