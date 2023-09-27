module InstructionMemory #(parameter DEPTH = 256, string FILENAME = "instructions.bin") (
    input logic [31:0] addr, // Address to read from
    output logic [31:0] instruction // Instruction read from memory
);

    logic [31:0] mem [0:DEPTH-1]; // Memory array

    assign instruction = mem[addr >> 2]; // byte-adress to word-address

    // Filling IM using the compiled instruction file
    initial begin
        integer file, i;
        file = $fopen(FILENAME, "rb");
        if (file) begin
            for (i = 0; i < DEPTH; i = i + 1) begin
                if (!$fread(mem[i], file)) break; // Exit the loop as soon as the file ends
            end
            $fclose(file);
        end else
            $fatal("Unable to open file %0s", FILENAME);
    end
endmodule