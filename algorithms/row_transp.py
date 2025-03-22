def row_gen_key(key: str) -> np.ndarray: # 3.3.1
    ascii_key = []
    new_key = []
    key_matrix = []

    # get rid of duplicates
    for x in key:
        if x not in new_key:
            new_key.append(x)
    # convert to ascii
    for i in new_key:
        ascii_key.append(ord(i))

    sorted_ascii = list(ascii_key)
    sorted_ascii.sort() # sorted ascendingly to determine order
    for i in sorted_ascii:
        key_matrix.append(ascii_key.index(i))

    return np.array(key_matrix)

def row_pad_text(plaintext: str, key: np.ndarray) -> str: # 3.3.2
    length = len(key)
    while len(plaintext) % length !=0:
        plaintext = plaintext+ 'x'
    return plaintext

def row_encrypt_single_stage(plaintext: str, key: np.ndarray) -> str:
    plaintext = row_pad_text(plaintext, key)
    # dimensions of block that I am seperating it into
    key_length = len(key)
    num_rows = len(plaintext) // key_length
    
    ciphertext = ""
    for k in key: # each number of the key
        for i in range(num_rows):
            position = i * key_length + k # i* key_length controls row count, k then indexes to 
                                          # correct cipher
            ciphertext += plaintext[position]
    
    return ciphertext

def row_decrypt_single_stage(ciphertext: str, key: np.ndarray) -> str:
    key_length = len(key)
    num_rows = len(ciphertext) // key_length
    
    # create an empty matrix to house the decrypted text
    matrix = [[''] * key_length for _ in range(num_rows)]

    # go column by column for decrypion into the matrix
    char_index = 0
    for k_index, k_value in enumerate(key):
        for i in range(num_rows):
            matrix[i][k_value] = ciphertext[char_index]
            char_index += 1

    # move lists of characters into the plaintext
    plaintext = ""
    for row in matrix:
        plaintext += ''.join(row)
    
    return plaintext

def row_encrypt(plaintext: str, key: str, stage: int) -> str:
    key_array = row_gen_key(key)
    
    ciphertext = row_encrypt_single_stage(plaintext, key_array)
    
    # second stage if required
    if stage > 1:
        ciphertext = row_encrypt_single_stage(ciphertext, key_array)
    
    return ciphertext

def row_decrypt(ciphertext: str, key: str, stage: int) -> str:

    key_array = row_gen_key(key)
    
    plaintext = row_decrypt_single_stage(ciphertext, key_array)
    
    # Second stage if required
    if stage > 1:
        plaintext = row_decrypt_single_stage(plaintext, key_array)
    
    # Remove padding 
    plaintext = plaintext.rstrip('x')
    
    return plaintext