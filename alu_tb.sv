module ALU_tb;

  // Declare signals for connecting to ALU module
  reg [31:0] operandA;
  reg [31:0] operandB;
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

  // Define a clock signal
  reg clk = 0;
  always #5 clk = ~clk; // Clock period of 10 time units

  // Test cases
  initial begin
    // Test case 1: Addition
    operandA = 10;
    operandB = 20;
    funct3 = 3'b000;
    funct7 = 0;
    #10; // Wait for 10 time units
    if (result !== 30) $display("Test case 1 failed");

    // Test case 2: Subtraction
    operandA = 50;
    operandB = 30;
    funct3 = 3'b000;
    funct7 = 1;
    #10;
    if (result !== 20) $display("Test case 2 failed");

    // Finish simulation
    $finish;
  end

  // Monitor and display results
  always @(posedge clk) begin
    $display("operandA = %d, operandB = %d, funct3 = %b, funct7 = %b, result = %d", operandA, operandB, funct3, funct7, result);
  end

endmodule
