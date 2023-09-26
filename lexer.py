import re

# Definición de patrones para tokens
token_patterns = [
    (r'LOAD', r'ld'),          # Instrucción de carga
    (r'STORE', r'st'),        # Instrucción de almacenamiento
    (r'REGISTER', r'r\d+'),    # Registro (r0, r1, r2, ...)
    (r'COMMA', r','),          # Coma para separar operandos
    (r'NEWLINE', r'\n'),       # Nueva línea para finalizar instrucciones
]

# Función para tokenizar el código fuente
def lexer(code):
    tokens = []
    while code:
        for token_type, pattern in token_patterns:
            match = re.match(pattern, code)
            if match:
                value = match.group(0)
                tokens.append((token_type, value))
                code = code[len(value):]
                break
        else:
            raise ValueError("No se pudo analizar el código: ", code)
    return tokens

# Ejemplo de código fuente Assembly
assembly_code = """
st r3, r4
""" 

# Tokeniza el código fuente
tokens = lexer(assembly_code)

# Imprime los tokens resultantes
for token_type, value in tokens:
    print(f'Token: {token_type}, Valor: {value}')
