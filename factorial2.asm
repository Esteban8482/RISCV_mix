.data
    .align 2
    .global num
num: .word 5

.text
    .align 2
    .global factorial
factorial:
    # Prologue
    addi    sp, sp, -8     # Hacer espacio en la pila
    sw      ra, 0(sp)      # Guardar el registro de retorno
    sw      s0, 4(sp)      # Guardar el registro de marco

    # Cuerpo de la función factorial
    lw      s0, 0(a0)      # Cargar n en s0
    li      t0, 1          # Cargar el valor 1 en t0
    beq     s0, t0, end_factorial   # if (n == 0 || n == 1) return 1
    
    subi    sp, sp, 4      # Hacer espacio en la pila para el argumento de la llamada recursiva
    addi    a0, s0, -1     # n - 1 como argumento para la llamada recursiva
    jal     ra, factorial  # Llamar recursivamente a factorial(n - 1)
    addi    sp, sp, 4      # Liberar el espacio de la pila utilizado para el argumento
    
    lw      t1, 0(a0)      # Cargar el valor de retorno de la llamada recursiva en t1
    mul     a0, s0, t1     # n * factorial(n - 1)
    j       end_factorial  # Saltar al final de la función factorial
    
end_factorial:
    # Epílogo
    lw      ra, 0(sp)      # Restaurar el registro de retorno
    lw      s0, 4(sp)      # Restaurar el registro de marco
    addi    sp, sp, 8      # Liberar espacio en la pila
    ret

    .align 2
    .global main
main:
    # Prologue
    addi    sp, sp, -4     # Hacer espacio en la pila
    sw      ra, 0(sp)      # Guardar el registro de retorno

    # Cuerpo de la función main
    la      a0, num        # Cargar la dirección de la variable num en a0
    jal     ra, factorial  # Llamar a la función factorial

    # Epílogo
    lw      ra, 0(sp)      # Restaurar el registro de retorno
    addi    sp, sp, 4      # Liberar espacio en la pila
    ret
