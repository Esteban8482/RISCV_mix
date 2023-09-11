module ALU_tb;

  // Define signals to connect to the ALU module
  reg [31:0] operandA, operandB;
  reg [2:0] funct3;
  reg funct7;
  wire [31:0] result;

  // Instantiate the ALU module
  ALU uut (
    .operandA(operandA),
    .operandB(operandB),
    .funct3(funct3),
    .funct7(funct7),
    .result(result)
  );

  // Clock generation
  reg clk = 0;
  always #10 clk = ~clk;

  // Test vectors
  initial begin
    // Test 1: Addition (funct3=000, funct7=0)
    operandA = 10;
    operandB = 20;
    funct3 = 3'b000;
    funct7 = 1'b0;
    #10;
    if (result != operandA + operandB) $display("Test 1 failed");

    // Test 2: Subtraction (funct3=000, funct7=1)
    operandA = 50;
    operandB = 30;
    funct3 = 3'b000;
    funct7 = 1'b1;
    #10;
    if (result != operandA - operandB) $display("Test 2 failed");

    // Test 3: Shift left (funct3=001)
    operandA = 8;
    operandB = 2;
    funct3 = 3'b001;
    funct7 = 0;
    #10;
    if (result != (operandA << operandB)) $display("Test 3 failed");

    // Test 4: Shift right (funct3=101, funct7=0)
    operandA = 32;
    operandB = 2;
    funct3 = 3'b101;
    funct7 = 0;
    #10;
    if (result != (operandA >> operandB)) $display("Test 4 failed");

    // Test 5: Shift signed (funct3=101, funct7=1)
    operandA = 16; // Positive number
    operandB = 2;
    funct3 = 3'b101;
    funct7 = 1'b1;
    #10;
    if (result != (operandA >>> operandB)) $display("Test 5_1 failed");

    operandA = -16; // Negative number
    operandB = 2;
    funct3 = 3'b101;
    funct7 = 1'b1;
    #10;
    if (result != (operandA >>> operandB)) $display("Test 5_2 failed");

    // Test 6: Shift unsigned (funct3=101, funct7=0)
    operandA = 32;
    operandB = 2;
    funct3 = 3'b101;
    funct7 = 0;
    #10;
    if (result != (operandA >> operandB)) $display("Test 6 failed");

    // Test 7: Logical AND (funct3=010)
    operandA = 5'b10101;
    operandB = 5'b11011;
    funct3 = 3'b010;
    funct7 = 1'b0;
    #10;
    if (result != (operandA & operandB)) $display("Test 7 failed");

    // Test 8: Logical OR (funct3=011)
    operandA = 5'b10101;
    operandB = 5'b11011;
    funct3 = 3'b011;
    funct7 = 1'b0;
    #10;
    if (result != (operandA | operandB)) $display("Test 8 failed");

    // Test 9: Logical XOR (funct3=100)
    operandA = 5'b10101;
    operandB = 5'b11011;
    funct3 = 3'b100;
    funct7 = 1'b0;
    #10;
    if (result != (operandA ^ operandB)) $display("Test 9 failed");


    $finish;
  end

  // Monitor for displaying results
  always @(posedge clk) begin
    $display("Result = %d", result);
  end

endmodule