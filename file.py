instructions=[
    {"inst" :"ADD", "type": "R", "opcode" :"0110011", "funct3": "000", "funct7": "0000000"},
    {"inst" :"SUB", "type": "R", "opcode" :"0110011", "funct3": "000", "funct7": "0010000"},
    {"inst" :"XOR", "type": "R", "opcode" :"0110011", "funct3": "100", "funct7": "0000000"},
    {"inst" :"OR", "type": "R", "opcode" :"0110011", "funct3": "110", "funct7":  "0000000"},
    {"inst" :"AND", "type": "R", "opcode" :"0110011", "funct3": "111", "funct7": "0000000"},
    {"inst" :"SLL", "type": "R", "opcode" :"0110011", "funct3": "001", "funct7": "0000000"},
    {"inst" :"SRL", "type": "R", "opcode" :"0110011", "funct3": "101", "funct7": "0010000"},
    {"inst" :"SRA", "type": "R", "opcode" :"0110011", "funct3": "101", "funct7": "0000000"},
    {"inst" :"SLT", "type": "R", "opcode" :"0110011", "funct3": "010", "funct7": "0000000"},
    {"inst" :"SLTU", "type": "R", "opcode" :"0110011", "funct3": "011", "funct7": "0000000"},

    {"inst" :"ADDI", "type": "I", "opcode" :"0010011", "funct3": "000", "funct7": "0000000"},
    {"inst" :"XORI", "type": "I", "opcode" :"0010011", "funct3": "100", "funct7": "0000000"},
    {"inst" :"ORI", "type": "I", "opcode" :"0010011", "funct3": "110", "funct7":  "0000000"},
    {"inst" :"ANDI", "type": "I", "opcode" :"0010011", "funct3": "111", "funct7": "0000000"},
    {"inst" :"SLLI", "type": "I", "opcode" :"0010011", "funct3": "001", "funct7": "0000000"},
    {"inst" :"SRLI", "type": "I", "opcode" :"0010011", "funct3": "101", "funct7": "0000000"},
    {"inst" :"SRAI", "type": "I", "opcode" :"0010011", "funct3": "101", "funct7": "0000000"},
    {"inst" :"SLTI", "type": "I", "opcode" :"0010011", "funct3": "010", "funct7": "0000000"},
    {"inst" :"SLTIU", "type": "I", "opcode" :"0010011", "funct3": "011", "funct7": "0000000"},
    {"inst" :"LB", "type": "I", "opcode" :"0000011", "funct3": "000", "funct7": "0000000"},
    {"inst" :"LH", "type": "I", "opcode" :"0000011", "funct3": "001", "funct7": "0000000"},
    {"inst" :"LW", "type": "I", "opcode" :"0000011", "funct3": "010", "funct7": "0000000"},
    {"inst" :"LBU", "type": "I", "opcode" :"0000011", "funct3": "100", "funct7":"0000000"},
    {"inst" :"LHU", "type": "I", "opcode" :"0000011", "funct3": "101", "funct7":"0000000"},

    {"inst" :"SB", "type": "S", "opcode" :"0100011", "funct3": "000", "funct7": "0000000"},
    {"inst" :"SH", "type": "S", "opcode" :"0100011", "funct3": "001", "funct7": "0000000"},
    {"inst" :"SW", "type": "S", "opcode" :"0100011", "funct3": "010", "funct7": "0000000"},

    {"inst" :"BEQ", "type": "B", "opcode" :"1100011", "funct3": "000", "funct7": "0000000"},
    {"inst" :"BNE", "type": "B", "opcode" :"1100011", "funct3": "001", "funct7": "0000000"},
    {"inst" :"BLT", "type": "B", "opcode" :"1100011", "funct3": "100", "funct7": "0000000"},
    {"inst" :"BGE", "type": "B", "opcode" :"1100011", "funct3": "101", "funct7": "0000000"},
    {"inst" :"BLTU", "type": "B", "opcode" :"1100011", "funct3": "110", "funct7": "0000000"},
    {"inst" :"BGEU", "type": "B", "opcode" :"1100011", "funct3": "111", "funct7": "0000000"},

    {"inst" :"JAL", "type": "J", "opcode" :"1101111", "funct3": "000", "funct7": "0000000"},
    {"inst" :"JALR", "type":"I", "opcode" :"1100111", "funct3": "000", "funct7": "0000000"},

    {"inst" :"LUI", "type": "U", "opcode" :"0110111", "funct3": "010", "funct7": "0000000"},
    {"inst" :"AUIPC", "type": "U", "opcode" :"0010111", "funct3": "010", "funct7": "0000000"},

    {"inst" :"ECALL", "type": "I", "opcode" :"1110011", "funct3": "000", "funct7": "0000000"},
    {"inst" :"EBREAK", "type": "I", "opcode" :"1110011", "funct3": "000", "funct7": "0000000"},
    ]
