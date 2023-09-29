module InstructionMemory #(parameter DEPTH = 256, string FILENAME = "instructions.bin") (
    input logic [31:0] addr, // Address to read from
    output logic [31:0] instruction // Instruction read from memory
);

    logic [31:0] mem [0:DEPTH-1]; // Memory array

    // 2 bits right shift
    assign instruction = mem[addr >> 2]; // byte-address to word-address

    initial begin
        integer file, i;
        file = $fopen(FILENAME, "rb");
        if (file) 
            begin
                for (i = 0; i < DEPTH; i = i + 1) begin
                    if (!$fread(mem[i], file)) break; // Break if end-of-file or reading error occurs
            end
            $fclose(file);
        end else
            $fatal("Unable to open file");
    end
endmodule

//TODO: que el traductor genere un archivo "instruction memory"
//TODO: el archivo que toma el traductor debe tener extension ".s48" o ".asm48"
//TODO: el archivo que retorna el traductor debe tener extension ".bin48"
//TODO: buscar "Verilator"
//TODO: Usar little endian como estandar
//TODO: Modulo en verilog que soporte las instrucciones tipo S, R, I. Sin incluir JAL y JALR (Entregable)