import numpy as np

def hex_to_matrix(hex_string):
    matrix = [[0,0],[0,0]]
    matrix[0][0] = int(hex_string[0], 16)
    matrix[0][1] = int(hex_string[1], 16)
    matrix[1][0] = int(hex_string[2], 16)
    matrix[1][1] = int(hex_string[3], 16)
    
    return matrix

def matrix_to_hex(matrix):
    hex_string = ""
    for i in range(2):
        for j in range(2):
            hex_string += format(matrix[i][j],'X')
    
    return hex_string

def generate_round_keys(key):
    key_matrix = hex_to_matrix(key)

    round_keys = [key_matrix]

    for i in range(3):
        new_key = [[0,0],[0,0]]

        for i in range(2):
            for j in range(2):
                
                value = round_keys[-1][i][j]
                shifted = ((value << 1) & 0xF) | ((value >> 3) & 0x1)
                new_key[i][j] = shifted
        round_keys.append(new_key)
    return round_keys

