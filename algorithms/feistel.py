def feistel(plain, key, decrypt=False):
    """
    A modified Feistel cipher is used to encrypt/decrypt a 16-bit message with a 16-bit key using 
    three rounds. 
    The round function is a plain XOR operation of the input and the most significant 
    (leftmost) subkey bits.
    Subkeys are generated by a circular 1-bit left shift for every round w.r.t. 
    to initial key (i.e. 1 bit shift for round 1, 2 bit shift for round 2 etc.). 
    K2 = 8E4316
    """
    #keep as numbers for ease of manipulation, don't need to convert to hex
    # Generate the subkeys using bit shifting
    subkeys = []
    for i in range(1, 4):
        # Create circular shift using bit operations
        subkey = ((key << i) | (key >> (16 - i))) & 0xFFFF
        subkeys.append((subkey >> 8) & 0xFF)

    print([hex(sk)[2:] for sk in subkeys])
    #for decrypt simply reverse keys
    if decrypt:
        subkeys.reverse()
        
    # Split plaintext into left and right halves (8 bits each)
    left = (plain >> 8) & 0xFF  #MSB
    right = plain & 0xFF #LSB
    
    # Perform the rounds
    for i in range(3):
        # Store current state for printing
        func = left ^ subkeys[i] ^ right
        left = right
        right = func

        print(format(right, 'x') + format(left, 'x'))
    
    # Combine left and right for final result (right is now left and vice versa)
    cipher = (right << 8) | left
    # Return the cipher text
    return hex(cipher)