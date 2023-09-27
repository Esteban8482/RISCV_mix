.data
n:      .word 12

.text
main:
    la t4, n                 # Load address of n into t4
    lw t5, 0(t4)             # Load n into t5
    
    li a0, 1                 # Initialize base matrix
    li a1, 1
    li a2, 1
    li a3, 0
    
    jal ra, matrix_power     # Call matrix_power with n stored in t5
    
    mv a0, a2                # Move result to a0
    
    # End execution
    li a7, 10
    ecall

matrix_power:
    li t0, 1                 # Load immediate 1 into t0 for comparison
    beq t5, t0, end_matrix_power  # If n == 1, just return the base matrix

    # Save return address and other registers
    addi sp, sp, -20         
    sw ra, 16(sp)            
    sw t5, 12(sp)             
    sw a0, 8(sp)             
    sw a1, 4(sp)             
    sw a3, 0(sp)

    # Check if n is odd
    andi t1, t5, 1           # t1 = n % 2

    # Divide n by 2
    srai t5, t5, 1
    jal ra, matrix_power

    # Square the result
    jal ra, matrix_square

    # If odd, multiply with base matrix
    beq t1, x0, end_recursive
    jal ra, matrix_multiply_base

end_recursive:
    lw ra, 16(sp)            # Restore return address
    addi sp, sp, 20          # Deallocate stack space

end_matrix_power:
    ret

matrix_multiply_base:
    # Multiply matrix in a0-a3 with base matrix
    
    li s9, 1                 # Load 1 into t6
    mul t2, a0, s9           # t2 = a0*1
    mul t3, a1, s9           # t3 = a1*1
    add t2, t2, t3           # t2 = a0 + a1 (new a0)
    
    mv t3, a0                # t3 = a0 (new a1)
    
    mul t4, a0, s9           # t4 = a0*1 (new a2)
    
    mv t5, a2                # t5 = a2 (new a3)
    
    # Store the results back to a0-a3
    mv a0, t2
    mv a1, t3
    mv a2, t4
    mv a3, t5
    
    ret


matrix_square:
    # Square matrix in a0-a3
    mul t2, a0, a0          # t2 = a0*a0
    mul t3, a1, a2          # t3 = a1*a2
    add t2, t2, t3          # t2 = a0*a0 + a1*a2 (new a0)
    
    mul t3, a0, a1          # t3 = a0*a1
    mul t4, a1, a3          # t4 = a1*a3
    add t3, t3, t4          # t3 = a0*a1 + a1*a3 (new a1)
    
    mul t4, a2, a0          # t4 = a2*a0
    mul t5, a3, a2          # t5 = a3*a2
    add t4, t4, t5          # t4 = a2*a0 + a3*a2 (new a2)
    
    mul t5, a2, a1          # t5 = a2*a1
    mul t6, a3, a3          # t6 = a3*a3
    add t5, t5, t6          # t5 = a2*a1 + a3*a3 (new a3)
    
    # Store the results back to a0-a3
    mv a0, t2
    mv a1, t3
    mv a2, t4
    mv a3, t5

    ret