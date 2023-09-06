module ALU (
  input [31:0] operandA, 
  input [31:0] operandB,
  input [2:0] funct3, 
  input funct7,  
  output reg [31:0] result, 
);

always @(*) begin
    // Perform the selected operation based on the funct3 and funct7
    case(funct3)
        // Type R instructions
        3'b000: // Addition and subtraction
            case(funct7)
                1'b0: // Addition
                    result = operandA + operandB;
                1'b1: // Subtraction
                    result = operandA - operandB;
        3'b001 // Shift left by operandB
            result = operandA << operandB;
        3'b101:
            case(funct7)
                1'b1: // Arithmetic shift right 
                    //TODO: Entender que chucha es el shift aritmetico
                    if (operandB > 0) begin
                        result = operandA >>> operandB;
                    // Llena los bits más significativos con el valor del bit de signo original.
                    if (operandA[31] == 1)
                        result = {32{1'b1}} & result;
                    else
                        result = {32{1'b0}} & result;
                    end else
                1'b0: // Logical shift right
                    result = operandA >> operandB;
        3'b010: // Logical AND
            result = operandA & operandB;
        3'b011: // Logical OR
            result = operandA | operandB;
        3'b100: // Logical XOR ~ Equality operation when denied
            result = operandA ^ operandB;
        default: // Default to zero
            result = 0;

        //TODO: Type I instructions
    endcase
end

endmodule
