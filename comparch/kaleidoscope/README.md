# Kaleidoscope

## Introduction (the langauge)

Kaleidoscope is a simple programming language designed to teach how to
implement all the components of a compiler. The language described here is an
adaptation of the one proposed in [this tutorial](https://llvm.org/docs/tutorial/). The old and mandatory example of computing the factorial of a given integer, say `n=5` is achieved by the following program.

```
    def factorial(n) {
        if (n = 0) { 
            1 
        } else { 
            n * factorial(n-1)
        }
    }
    factorial(5)
```

We use the program above to describe the language constructs. In the first
place, Kaleidoscope supports function definitions, function invocation and
conditional execution via the `if` statement. Apart from these constructs, the
language supports arithmetic operations like addition, multiplication,
subtraction and division. Logical operations like comparisons (i.e. =, <=, <, >, >= ) are also supported.

Tha language is so simple that variables can be only of one type: integers. At this point you will think this is a silly language, however, think about this twice and have a look at the [lambda calculus](https://en.wikipedia.org/wiki/Lambda_calculus).

For the program above here is the corresponding AST:![](./factorial.png)

### Other programs written in Kaleidoscope
- [Fibonacci](./examples/fib.kl)
- [The constant program](./examples/constant.kl)

## The compiler

The following documents will provide a tutorial of the step by step design and
construction of a compiler for Kaleidoscope. They are inline with the notions
taught in a typical course on compilers.

- Lexical analysis
- Syntactic analysis
- Semantic analysis
- Code generation

## The architecture

Kaleidoscope is intended to be executed on real hardware. To that end we
provide the design of a hardware architecture designed to execute the programs. In order to try out the compiler a simulator can be used to test the generated code [MIPS](./spim.md).provide the design of a hardware architecture designed to execute the programs. In order to try out the compiler a simulator can be used to test the generated code [MIPS](./spim.md).

### Architecture description
We target a MIPS architecture and initially we will use only two registers:

- `$a0` which is the accumulator register. All the operations will use this register to return.
- `$sp` is the **stack pointer**. A stack will be used to store all the intermediate values during the execution of a program.
- `$t1` is a temporary register.

Apart from the registers we use a limitted set of instructions:
- `lw reg_1 offset(reg_2)`: load a word from address `reg_2 + offset` into `reg_1`
- `add reg_1 reg_2 reg_3`: stores `reg_2 + reg_3` into `reg_1`.

## Future
The architecture implements a subset of the SPARC v8 instruction set and hence any [simulator](https://github.com/hugsy/cemu) can be used to test the compiler output.

However, no real hardware is needed as our compiler produces assembly code 
