module data_memory #(
    parameter ADDR_WIDTH = 10 // Address width, adjust as necessary
) (
    input logic clk,                      // Clock
    input logic rst,                      // Reset
    input logic wr_en,                    // Write enable
    input logic [ADDR_WIDTH-1:0] address, // Address
    input logic [31:0] wr_data,           // Write Data
    output logic [31:0] rd_data           // Read Data
);

    // Declare the memory as a two-dimensional packed array
    logic [31:0] memory [(1 << ADDR_WIDTH) - 1:0];

    integer i; // Index variable for the loop
    
    always_ff @(posedge clk or posedge rst) begin
        if (rst) begin
            // Initialize all memory locations to zero during reset
            for (i = 0; i < (1 << ADDR_WIDTH); i = i + 1) begin
                memory[i] <= 32'b0;
            end
        end else if (wr_en) begin
            // Write operation
            memory[address] <= wr_data;
        end
    end
    
    // Read operation (Non-blocking)
    assign rd_data = memory[address];

endmodule