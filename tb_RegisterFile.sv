module tb_RegisterFile;

  reg clk;
  reg rst;
  reg we;
  reg [4:0] wrAddr;
  reg [4:0] rdAddr1;
  reg [4:0] rdAddr2;
  reg [31:0] wrData;
  wire [31:0] rdData1;
  wire [31:0] rdData2;

  // Instantiate the RegisterFile module
  RegisterFile uut (
    .clk(clk),
    .rst(rst),
    .we(we),
    .wrAddr(wrAddr),
    .rdAddr1(rdAddr1),
    .rdAddr2(rdAddr2),
    .wrData(wrData),
    .rdData1(rdData1),
    .rdData2(rdData2)
  );

  // Clock Generation
  initial begin
    clk = 0;
    forever #5 clk = ~clk;
  end

  // Test Procedure
  initial begin
    // Initialize
    rst = 1;
    we = 0;
    wrAddr = 0;
    rdAddr1 = 0;
    rdAddr2 = 0;
    wrData = 0;
    #10;
    
    // Release Reset
    rst = 0;
    #10;
    
    // Write to Register 1
    we = 1;
    wrAddr = 5'b00001; // Write to register x1
    wrData = 32'hDEADBEEF;
    #10;
    
    // Disable Write Enable
    we = 0;
    #10;
    
    // Read from Register 1
    rdAddr1 = 5'b00001; // Read from register x1
    #10;
    
    // Check the Read Data
    if(rdData1 === 32'hDEADBEEF)
      $display("Read Test Passed!");
    else
      $display("Read Test Failed! Expected: %h, Received: %h", 32'hDEADBEEF, rdData1);
    
    // Read from Register 0 (should be zero)
    rdAddr1 = 5'b00000; // Read from register x0
    #10;
    
    // Check the Read Data
    if(rdData1 === 32'h00000000)
      $display("Read Zero Register Test Passed!");
    else
      $display("Read Zero Register Test Failed! Expected: %h, Received: %h", 32'h00000000, rdData1);

    // End Simulation
    $finish;
  end
endmodule