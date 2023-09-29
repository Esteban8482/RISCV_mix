module tb_data_memory;

    reg clk;
    reg rst;
    reg wr_en;
    reg [9:0] address;
    reg [31:0] wr_data;
    wire [31:0] rd_data;

    // Instantiate the data_memory module
    data_memory uut (
        .clk(clk),
        .rst(rst),
        .wr_en(wr_en),
        .address(address),
        .wr_data(wr_data),
        .rd_data(rd_data)
    );

    // Clock generation
    always #2.5 clk = ~clk;

    initial begin
        // Specify the name of the VCD file
        $dumpfile("dump.vcd");
        
        // Dump all variables in the testbench and the instantiated module
        $dumpvars(0, tb_data_memory);

        // Initialize signals
        clk = 0;
        rst = 1;
        wr_en = 0;
        address = 0;
        wr_data = 0;

        // Apply reset
        #5 rst = 0;
        
        // Perform write operation to address 10
        address = 10;
        wr_data = 32'hDEADBEEF;
        wr_en = 1;
        #5;
        
        // Perform read operation from address 10
        wr_en = 0;
        #5;
        $display("Time: %0dns, Read Data from Address %0d: %h", $time, address, rd_data);

        // Perform write operation to address 20
        address = 20;
        wr_data = 32'h12345678;
        wr_en = 1;
        #5;

        // Perform read operation from address 20
        wr_en = 0;
        #5;
        $display("Time: %0dns, Read Data from Address %0d: %h", $time, address, rd_data);

        // Perform read operation from address 10 again
        address = 10;
        #5;
        $display("Time: %0dns, Read Data from Address %0d: %h", $time, address, rd_data);

        // End simulation
        $finish;
    end

endmodule