.data
n: .word 5          # Factorial to calculate

.text
main:
    la t0, n        # Load the address of the n word in t0
    lw a0, 0(t0)    # Load the value of n into a0
    li a1, 1        

factorial_loop:
    beq a0, x0, end_factorial  # If a0 is zero, then exit loop
    mul a1, a1, a0             # Multiply current factorial result with current number
    addi a0, a0, -1            # Decrement a0
    beq x0, x0, factorial_loop # back to the loop

end_factorial: