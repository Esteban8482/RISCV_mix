.data
n: .word 8

.text
main:
    la t0, n
    lw a0, 0(t0)
    jal ra, factorial
    
    addi a1, a0, 0
    addi a0, x0, 1
    ecall # Print Result
    
    addi a0, x0, 10
    ecall # Exit

factorial:
    li a2, 1       # Load immediate value 1 into a2
    li t1, 1       # Load immediate value 1 into t1 (used as a loop counter)
loop:
    beq a0, x0, end_factorial  # If a0 equals zero, exit loop
    mul a2, a2, a0  # Multiply a2 by a0 and store result in a2
    sub a0, a0, t1  # Decrement a0 by 1 using t1 as an immediate
    j loop           # Jump back to loop

end_factorial:
    mv a0, a2        # Move the factorial result in a2 to a0
    ret