module ALU (
  input logic [31:0] operandA, 
  input logic [31:0] operandB, 
  input logic [2:0] funct3, // Operation selector 1
  input logic funct7, // Operation selector 2
  output logic [31:0] result, 
);

always @(*) begin
    case(funct3)
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
                1'b1: // Shift signed
                    if (operandB > 0) begin
                        result = operandA >>> operandB;
                        if (operandA[31] == 1)
                            result = {32{1'b1}} & result;
                        else
                            result = {32{1'b0}} & result;
                        end else
                1'b0: // Shift unsigned
                    result = operandA >> operandB;
        3'b010: // Logical AND
            result = operandA & operandB;
        3'b011: // Logical OR
            result = operandA | operandB;
        3'b100: // Logical XOR ~ Equality operation when denied
            result = operandA ^ operandB;
        default: // Default to zero
            result = 0;
    endcase
end

endmodule
