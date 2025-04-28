key = "D93B"
sbox2 = [
    ['B', 'C', 'A', '8'],
    ['D', '2', '6', 'F'],
    ['3', 'E', '0', '4'],
    ['5', '9', '7', '1']
]

isbox2 = [
    ['A', 'F', '5', '8'],
    ['B', 'C', '6', 'E'],
    ['3', 'D', '2', '0'],
    ['1', '4', '9', '7']
]

def hex_to_matrix(hex_string):
    """Convert a 16-bit hex string to a 2x2 matrix with 4-bit elements."""
    # Ensure the hex string is 4 characters (16 bits)
    if len(hex_string) != 4:
        raise ValueError("Input hex string must be 4 characters (16 bits)")
    
    # Create a 2x2 matrix
    matrix = [[0, 0], [0, 0]]
    matrix[0][0] = int(hex_string[0], 16)
    matrix[0][1] = int(hex_string[1], 16)
    matrix[1][0] = int(hex_string[2], 16)
    matrix[1][1] = int(hex_string[3], 16)
    
    return matrix

def matrix_to_hex(matrix):
    """Convert a 2x2 matrix with 4-bit elements to a 16-bit hex string."""
    hex_string = ""
    for i in range(2):
        for j in range(2):
            hex_string += format(matrix[i][j], 'X')
    
    return hex_string

def generate_round_keys(key):
    """Generate round keys by applying incremental circular 1-bit left shift."""
    # Convert the hex key to a matrix
    key_matrix = hex_to_matrix(key)
    
    # Generate round keys for 3 rounds
    round_keys = [key_matrix]
    
    for r in range(3):
        # Create a new matrix for the next round key
        new_key = [[0, 0], [0, 0]]
        
        # Apply incremental circular 1-bit left shift to each element
        for i in range(2):
            for j in range(2):
                # Get the current element value
                value = round_keys[-1][i][j]
                
                # Apply circular left shift (4-bit values)
                shifted = ((value << 1) & 0xF) | ((value >> 3) & 0x1)
                
                # Store the shifted value
                new_key[i][j] = shifted
        
        round_keys.append(new_key)
    
    return round_keys