.data
baseMatrix:     .word 1, 1, 1, 0

.text
main:
    # Setting n directly in the program. Here, we're setting it to 10.
    li a0, 10               # a0 will now have the value 10 (Fibonacci position)

    li a1, 0                # a1 is used to store the Fibonacci number
    li a2, 1                # a2 is used to store the Fibonacci number
    li a3, 1                # Counter for the loop, initialize with 1 as fib(1) and fib(2) are known

fibLoop:
    beq a3, a0, endLoop     # If a3 (counter) is equal to a0 (n), exit loop
    addi a3, a3, 1           # Increment counter

    # Matrix multiplication specific to base matrix {{1,1}, {1,0}}
    # Here, I'm simplifying the multiplication for this specific matrix
    mv a4, a2               # Copy the previous Fibonacci number
    add a2, a2, a1          # New Fibonacci number = previous + one before previous
    mv a1, a4               # Update the one before previous Fibonacci number

    beq zero, zero, fibLoop

endLoop:
    mv a0, a2               # Store the result in a0

    # At this point, the Fibonacci number for position 10 is in the a0 register

    # Exit
    li a7, 10               # a7 stores the system call number. 10 is for program termination.
    ecall                   # System call
