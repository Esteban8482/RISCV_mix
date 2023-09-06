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
        3'b000: // Addition and subtraction
            case(funct7)
            1'b0: // Addition
                result = operandA + operandB;
            1'b1: // Subtraction
                result = operandA - operandB;
        3'b001 // Shift left by operandB
            result = operandA << operandB; 
        3'b010: // Logical AND
            result = operandA & operandB;
        3'b011: // Logical OR
            result = operandA | operandB;
        3'b100: // Logical XOR
            result = operandA ^ operandB;
        3'b101: // Shift left by one
            result = operandA << 1;
        3'b110: // Shift right by one
            result = operandA >> 1;
        default: // Default to zero
            result = 0;
    endcase
end

endmodule
