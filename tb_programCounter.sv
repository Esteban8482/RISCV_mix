module tb_program_counter;

    reg clk;
    reg rst;
    reg enable;
    reg [31:0] jump_addr;
    wire [31:0] pc_addr;

    // Instantiate the program_counter module
    program_counter uut (
        .clk(clk),
        .rst(rst),
        .enable(enable),
        .jump_addr(jump_addr),
        .pc_addr(pc_addr)
    );

    // Clock Generation
    always #5 clk = ~clk;

    initial begin
        // Specify the name of the VCD file
        $dumpfile("program_counter_dump.vcd");
        
        // Dump all variables in the testbench and the instantiated module
        $dumpvars(0, tb_program_counter);

        // Initialize Signals
        clk = 0;
        rst = 1;
        enable = 0;
        jump_addr = 0;
        
        // Apply Reset
        #10 rst = 0;
        
        // Observe the sequential increment of the PC
        #50;
        
        // Perform a jump
        enable = 1;
        jump_addr = 32;
        #10;
        
        // Deassert enable and observe PC
        enable = 0;
        #50;
        
        // End simulation
        $finish;
    end
    
endmodule
