.data
baseMatrix:     .word 1, 1, 1, 0

.text
main:
    li a0, 10               # fibonacci position to find

    li a1, 0                # First fibonacci position
    li a2, 1                # Second fibonacci position
    li a3, 1                # Counter

fibLoop:
    beq a3, a0, endLoop     # Loop exit condition
    addi a3, a3, 1           # Increment counter

    mv a4, a2               # Copy the previous Fibonacci number
    add a2, a2, a1          # New Fibonacci number = previous + one before previous
    mv a1, a4               # Update the one before previous Fibonacci number

    beq zero, zero, fibLoop # Back to the beginning of the loop

endLoop:
    mv a0, a2               # Store the result in a0