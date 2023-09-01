module ALU (
  input [31:0] operandA, 
  input [31:0] operandB, 
  input [2:0]  opcode,   
  output reg [31:0] result, 
  output reg zeroFlag,     // Set if result is zero
  output reg carryFlag,    // Set if there's a carry-out (for addition)
  output reg overflowFlag  // Set if there's an overflow
);

always @(*) begin
    // Default values
    result = 0;
    zeroFlag = 0;
    carryFlag = 0;
    overflowFlag = 0;

    // Perform the selected operation based on the opcode
    case(opcode)
        3'b000: // Addition
            result = operandA + operandB;
            // Check for carry and overflow
            carryFlag = (result < operandA) || (result < operandB);
            overflowFlag = ((operandA[31] == operandB[31]) && (operandA[31] != result[31]));
        3'b001: // Subtraction
            result = operandA - operandB;
            // Check for carry and overflow
            carryFlag = (operandA < operandB) || (operandB > result);
            overflowFlag = ((operandA[31] != operandB[31]) && (operandA[31] != result[31]));
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

    // Set zeroFlag if the result is zero
    zeroFlag = (result == 0);
end

endmodule
