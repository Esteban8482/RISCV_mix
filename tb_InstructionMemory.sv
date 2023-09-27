module tb_InstructionMemory;

    reg [31:0] addr; 
    wire [31:0] instruction;
    
    // Instantiate the InstructionMemory module with DEPTH=256 and FILENAME="instructions.bin"
    InstructionMemory #(256, "instructions.bin") uut (
        .addr(addr),
        .instruction(instruction)
    );
    
    initial begin
        // Test with different addresses
        addr = 4'b0000;  // Word address 0 (Byte address 0)
        #10;  // Delay for 10 time units
        $display("Instruction at address %0d: %h", addr, instruction);
        
        addr = 4'b0001;  // Word address 1 (Byte address 4)
        #10;
        $display("Instruction at address %0d: %h", addr, instruction);
        
        addr = 4'b0010;  // Word address 2 (Byte address 8)
        #10;
        $display("Instruction at address %0d: %h", addr, instruction);
        
        // Add more test cases as needed
        
        $finish;  // End the simulation
    end

endmodule
