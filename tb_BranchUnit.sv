module tb_BranchUnit;

    // Parámetros de tiempo
    parameter CLK_PERIOD = 10; // Asumiendo un período de reloj de 10ns

    // Señales de prueba
    logic clk;
    logic [31:0] operandA;
    logic [31:0] operandB;
    logic [2:0]  branchType;
    logic [31:0] jumpAddr;
    logic        takeBranch;
    logic [31:0] branchTarget;

    // Instancia del módulo BranchUnit
    BranchUnit uut (
        .operandA(operandA),
        .operandB(operandB),
        .branchType(branchType),
        .jumpAddr(jumpAddr),
        .takeBranch(takeBranch),
        .branchTarget(branchTarget)
    );

    // Generador de reloj
    always begin
        # (CLK_PERIOD / 2) clk = ~clk;
    end

    // Procedimiento de prueba
    initial begin
        // Inicialización
        clk = 0;
        operandA = 32'd10;
        operandB = 32'd20;
        branchType = 3'b000; // BEQ
        jumpAddr = 32'd100;

        // Espera un ciclo de reloj
        #CLK_PERIOD;

        // Prueba BEQ (Branch if Equal) - No debe tomar el branch
        $display("Testing BEQ with operandA = %0d, operandB = %0d", operandA, operandB);
        #CLK_PERIOD;
        $display("takeBranch = %0d, branchTarget = %0d", takeBranch, branchTarget);

        // Cambia operandB para que sea igual a operandA
        operandB = 32'd10;

        // Espera un ciclo de reloj
        #CLK_PERIOD;

        // Prueba BEQ (Branch if Equal) - Debe tomar el branch
        $display("Testing BEQ with operandA = %0d, operandB = %0d", operandA, operandB);
        #CLK_PERIOD;
        $display("takeBranch = %0d, branchTarget = %0d", takeBranch, branchTarget);

        // Puedes agregar más pruebas para otros tipos de operaciones de branch aquí

        // Finaliza la simulación
        $finish;
    end

endmodule
