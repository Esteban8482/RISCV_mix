instructions = [
    0x20100013,  # addi x0, x0, 32
    0x20200093,  # addi x1, x0, 32
    0x00208033,  # add x2, x1, x0
    # Add more instructions as needed
]

with open('instructions.bin', 'wb') as f:
    for instruction in instructions:
        f.write(instruction.to_bytes(4, 'big'))  # Write each instruction as 4 bytes (32 bits) in big endian
