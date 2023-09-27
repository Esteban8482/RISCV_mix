module tb_InstructionMemory;

    reg [31:0] addr;  // 32-bit address for IM
    wire [31:0] instruction;
    
    // Instantiate the InstructionMemory module
    InstructionMemory uut (
        .addr(addr),
        .instruction(instruction)
    );
    
    initial begin
        // Test with different addresses
        addr = 32'b00000000000000000000000000000000;  // Byte address 0 (Word address 0)
        #10;  // Delay for 10 time units
        $display("Instruction at address %0d: %h", addr, instruction);
        
        addr = 32'b00000000000000000000000000000100;  // Byte address 4 (Word address 1)
        #10;
        $display("Instruction at address %0d: %h", addr, instruction);
        
        addr = 32'b00000000000000000000000000001000;  // Byte address 8 (Word address 2)
        #10;
        $display("Instruction at address %0d: %h", addr, instruction);
        
        // Add more test cases as needed
        
        $finish;  // End the simulation
    end

endmodule
