import json

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

register_map = {
    "x0": "00000", "zero": "00000",
    "x1": "00001", "ra": "00001",
    "x2": "00010", "sp": "00010",
    "x3": "00011", "gp": "00011",
    "x4": "00100", "tp": "00100",
    "x5": "00101", "t0": "00101",
    "x6": "00110", "t1": "00110",
    "x7": "00111", "t2": "00111",
    "x8": "01000", "s0": "01000", "fp": "01000",
    "x9": "01001", "s1": "01001",
    "x10": "01010", "a0": "01010",
    "x11": "01011", "a1": "01011",
    "x12": "01100", "a2": "01100",
    "x13": "01101", "a3": "01101",
    "x14": "01110", "a4": "01110",
    "x15": "01111", "a5": "01111",
    "x16": "10000", "a6": "10000",
    "x17": "10001", "a7": "10001",
    "x18": "10010", "s2": "10010",
    "x19": "10011", "s3": "10011",
    "x20": "10100", "s4": "10100",
    "x21": "10101", "s5": "10101",
    "x22": "10110", "s6": "10110",
    "x23": "10111", "s7": "10111",
    "x24": "11000", "s8": "11000",
    "x25": "11001", "s9": "11001",
    "x26": "11010", "s10": "11010",
    "x27": "11011", "s11": "11011",
    "x28": "11100", "t3": "11100",
    "x29": "11101", "t4": "11101",
    "x30": "11110", "t5": "11110",
    "x31": "11111", "t6": "11111"
}


def register_to_binary(register_name):
    # Obtiene el registro en su nombre binario
    binary_code = register_map.get(register_name)
    
    # Si no se encuentra el registro, se lanza un error
    if binary_code is None:
        raise ValueError(f"Registro '{register_name}' no definido.")
    
    return binary_code


def immediate_to_binary(value, bit_length):
    # El valor inmediato se convierte a binario con el largo especificado por el tipo de instruccion
     return format(int(value), f'0{bit_length}b') 

def to_upper(instruction, args):
    return instruction.upper(), args

def compile_instruction(instruction, args):
    inst_details = next((inst for inst in instructions if inst['inst'] == instruction), None)
    if not inst_details:
        return None

    if inst_details["type"] == "R":
        return inst_details["funct7"] + register_to_binary(args[2]) + register_to_binary(args[1]) + inst_details["funct3"] + register_to_binary(args[0]) + inst_details["opcode"]
    
    elif inst_details["type"] == "I":
        return immediate_to_binary(args[2], 12) + register_to_binary(args[1]) + inst_details["funct3"] + register_to_binary(args[0]) + inst_details["opcode"]
    
    elif inst_details["type"] == "S":
        return immediate_to_binary(args[2], 7) + immediate_to_binary(args[1], 5) + register_to_binary(args[1]) + inst_details["funct3"] + register_to_binary(args[0]) + inst_details["opcode"]
    
    elif inst_details["type"] == "B":
        # Asumiendo que args[2] es un valor inmediato
        return immediate_to_binary(args[2], 12) + register_to_binary(args[1]) + register_to_binary(args[0]) + inst_details["funct3"] + inst_details["opcode"]
    
    elif inst_details["type"] == "J":
        # Asumiendo que args[1] es un valor inmediato
        return immediate_to_binary(args[1], 20) + register_to_binary(args[0]) + inst_details["opcode"]
    
    elif inst_details["type"] == "U":
        # Asumiendo que args[1] es un valor inmediato
        return immediate_to_binary(args[1], 20) + register_to_binary(args[0]) + inst_details["opcode"]
    
    else:
        return None

def compile_s48_to_binary(filepath):
    with open(filepath, "r") as file:
        lines = file.readlines()

    parsed_instructions = []
    for line in lines:
        components = line.strip().split()
        if components:
            instruction_name = components[0]
            args = [arg.replace(",", "") for arg in components[1:]]
            parsed_instructions.append((instruction_name, args))

    upper_instructions = [to_upper(inst, args) for inst, args in parsed_instructions]
    compiled_instructions = [compile_instruction(inst, args) for inst, args in upper_instructions]
    return compiled_instructions

# Test the function
output = compile_s48_to_binary("instructionSample.s48")
print(output)