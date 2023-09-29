def assemble(instruction):
    opcode_map = {
        'add': '0110011',
        'sub': '0110011',
        'lw': '0000011',
        'sw': '0100011',
        'lui': '0110111'
    }
    
    funct3_map = {
        'add': '000',
        'sub': '000',
        'lw': '010',
        'sw': '010',
    }
    
    funct7_map = {
        'add': '0000000',
        'sub': '0100000'
    }
    
    register_map = {
        'zero': '00000',
        'ra': '00001',
        'sp': '00010',
        'gp': '00011',
        'tp': '00100',
        't0': '00101',
        't1': '00110',
        't2': '00111',
        's0': '01000',
        's1': '01001',
        'a0': '01010',
        'a1': '01011',
        'a2': '01100',
        'a3': '01101',
        'a4': '01110',
        'a5': '01111',
        'a6': '10000',
        'a7': '10001',
        's2': '10010',
        's3': '10011',
        's4': '10100',
        's5': '10101',
        's6': '10110',
        's7': '10111',
        's8': '11000',
        's9': '11001',
        's10': '11010',
        's11': '11011',
        't3': '11100',
        't4': '11101',
        't5': '11110',
        't6': '11111',
    }

    tokens = instruction.split()
    opcode = tokens[0]
    
    if opcode in ['add', 'sub']:
        rd = register_map[tokens[1]]
        rs1 = register_map[tokens[2]]
        rs2 = register_map[tokens[3]]
        funct3 = funct3_map[opcode]
        funct7 = funct7_map[opcode]
        return f'{funct7}{rs2}{rs1}{funct3}{rd}{opcode_map[opcode]}'
    
    elif opcode == 'lw':
        rd = register_map[tokens[1]]
        offset, rs1 = tokens[2].split('(')
        rs1 = rs1.rstrip(')')
        offset = format(int(offset), '012b')
        funct3 = funct3_map[opcode]
        return f'{offset}{register_map[rs1]}{funct3}{rd}{opcode_map[opcode]}'

    elif opcode == 'sw':
        offset, rs1 = tokens[1].split('(')
        rs1 = rs1.rstrip(')')
        rs2 = register_map[tokens[2]]
        funct3 = funct3_map[opcode]
        offset = format(int(offset), '012b')
        return f'{offset[:7]}{rs2}{register_map[rs1]}{funct3}{offset[7:]}{opcode_map[opcode]}'
    
    elif opcode == 'lui':
        rd = register_map[tokens[1]]
        immediate = format(int(tokens[2]), '020b')
        return f'{immediate}{rd}{opcode_map[opcode]}'
    
    else:
        raise ValueError(f"Unsupported opcode {opcode}")


instruction = 'add t0 s1 s2'  # Replace with your instruction.
try:
    binary_instruction = assemble(instruction)
    print(f"{instruction} -> {binary_instruction}")
except ValueError as e:
    print(e)