def right_rotate(value, n, bits=64):
    """Right rotate a value by n positions"""
    return ((value >> n) | (value << (bits - n))) & ((1 << bits) - 1)

def sha512(message):
    """
    Implements SHA-512 hash function
    
    Args:
        message: The input message as a hexadecimal string
    
    Returns:
        The SHA-512 hash digest as a hexadecimal string
    """
    # Constants
    n_blocks = 5  # Number of blocks
    n_P_bits = 1024  # Bits per block
    n_H_bits = 512  # Output hash size in bits
    
    # Initial hash values (in hex)
    a_hex = '6A09E667F3BCC908'
    b_hex = 'BB67AE8584CAA73B'
    c_hex = '3C6EF372FE94F82B'
    d_hex = 'A54FF53A5F1D36F1'
    e_hex = '510E527FADE682D1'
    f_hex = '9B05688C2B3E6C1F'
    g_hex = '1F83D9ABFB41BD6B'
    h_hex = '5BE0CD19137E2179'
    
    # Convert initial hash values to integers
    a = int(a_hex, 16)
    b = int(b_hex, 16)
    c = int(c_hex, 16)
    d = int(d_hex, 16)
    e = int(e_hex, 16)
    f = int(f_hex, 16)
    g = int(g_hex, 16)
    h = int(h_hex, 16)
    
    # SHA-512 round constants (K)
    K = [
        0x428A2F98D728AE22, 0x7137449123EF65CD, 0xB5C0FBCFEC4D3B2F, 0xE9B5DBA58189DBBC, 0x3956C25BF348B538, 
        0x59F111F1B605D019, 0x923F82A4AF194F9B, 0xAB1C5ED5DA6D8118, 0xD807AA98A3030242, 0x12835B0145706FBE, 
        0x243185BE4EE4B28C, 0x550C7DC3D5FFB4E2, 0x72BE5D74F27B896F, 0x80DEB1FE3B1696B1, 0x9BDC06A725C71235,  
        0xC19BF174CF692694, 0xE49B69C19EF14AD2, 0xEFBE4786384F25E3, 0x0FC19DC68B8CD5B5, 0x240CA1CC77AC9C65,  
        0x2DE92C6F592B0275, 0x4A7484AA6EA6E483, 0x5CB0A9DCBD41FBD4, 0x76F988DA831153B5, 0x983E5152EE66DFAB,  
        0xA831C66D2DB43210, 0xB00327C898FB213F, 0xBF597FC7BEEF0EE4, 0xC6E00BF33DA88FC2, 0xD5A79147930AA725, 
        0x06CA6351E003826F, 0x142929670A0E6E70, 0x27B70A8546D22FFC, 0x2E1B21385C26C926, 0x4D2C6DFC5AC42AED, 
        0x53380D139D95B3DF, 0x650A73548BAF63DE, 0x766A0ABB3C77B2A8, 0x81C2C92E47EDAEE6, 0x92722C851482353B,  
        0xA2BFE8A14CF10364, 0xA81A664BBC423001, 0xC24B8B70D0F89791, 0xC76C51A30654BE30, 0xD192E819D6EF5218,  
        0xD69906245565A910, 0xF40E35855771202A, 0x106AA07032BBD1B8, 0x19A4C116B8D2D0C8, 0x1E376C085141AB53,  
        0x2748774CDF8EEB99, 0x34B0BCB5E19B48A8, 0x391C0CB3C5C95A63, 0x4ED8AA4AE3418ACB, 0x5B9CCA4F7763E373,  
        0x682E6FF3D6B2B8A3, 0x748F82EE5DEFB2FC, 0x78A5636F43172F60, 0x84C87814A1F0AB72, 0x8CC702081A6439EC,  
        0x90BEFFFA23631E28, 0xA4506CEBDE82BDE9, 0xBEF9A3F7B2C67915, 0xC67178F2E372532B, 0xCA273ECEEA26619C,  
        0xD186B8C721C0C207, 0xEADA7DD6CDE0EB1E, 0xF57D4F7FEE6ED178, 0x06F067AA72176FBA, 0x0A637DC5A2C898A6,  
        0x113F9804BEF90DAE, 0x1B710B35131C471B, 0x28DB77F523047D84, 0x32CAAB7B40C72493, 0x3C9EBE0A15C9BEBC,  
        0x431D67C49C100D4C, 0x4CC5D4BECB3E42B6, 0x597F299CFC657E2A, 0x5FCB6FAB3AD6FAEC, 0x6C44198C4A475817
    ]
    
    # Convert the input message from hex to bytes
    # Note: in a full implementation, we'd handle padding here
    message_bytes = bytes.fromhex(message)
    
    # Expected output hashes for each block
    expected_outputs = [
        "24A8EE18E6400B0054F0A4C70F5751331546226CCFE536D537BCC2D99F30296134C58B14CA3255FE30DE38282B99613860F22DBD5A920C6627E20A28F7EC399D",
        "0B5A1271F9A4660B89102B3ECB46E7E5635D2B67A0551FD76544CE3DA459E6ADF6221BC81EA37DF0DFC01503B3D9F1D10DD3D6C2383E002ACB2142A057202067",
        "9E18C616FD40D405E1DCD2D6D75B4F55B472C78EA246239C3A66AC2B4F0451F22E3F01644424DB339FE6A8E89F7BFD00BF7FE19CF26E3919743515A6146E6805",
        "F44DE795CD4B4BD695C7B8543D2C113B6E3D80074198059BCC3206AAA4B01C7C1F45E3B77CD7665E27FA9BE213024ECED5349DB054D086CAB94CB99F96324516",
        "CD71BEAE4A9AA8339B2653B7EA7ED9EF3F92CB1B4AEF4382622ACD0EA53BA22BF18427D2DE86248A52D6AB1A730487FD95548FC9C5D6A7590D805998FBA21B76"
    ]
    
    # Process each block
    results = []
    
    for block_num in range(n_blocks):
        # Get the segment of the message for this block
        start_byte = block_num * (n_P_bits // 8)
        end_byte = start_byte + (n_P_bits // 8)
        block = message_bytes[start_byte:end_byte]
        
        # Initialize working variables with current hash values
        a_val, b_val, c_val, d_val, e_val, f_val, g_val, h_val = a, b, c, d, e, f, g, h
        
        # Prepare the message schedule (80 64-bit words)
        w = [0] * 80
        
        # Fill the first 16 words with the block data
        for i in range(16):
            w[i] = int.from_bytes(block[i*8:(i+1)*8], byteorder='big')
        
        # Extend the first 16 words to fill the remaining words
        for i in range(16, 80):
            s0 = right_rotate(w[i-15], 1) ^ right_rotate(w[i-15], 8) ^ (w[i-15] >> 7)
            s1 = right_rotate(w[i-2], 19) ^ right_rotate(w[i-2], 61) ^ (w[i-2] >> 6)
            # As per disclaimer: mod used instead of add mod
            w[i] = (w[i-16] + s0 + w[i-7] + s1) % (1 << 64)  
        
        # Main compression loop
        for i in range(80):
            # SHA-512 compression function operations
            S1 = right_rotate(e_val, 14) ^ right_rotate(e_val, 18) ^ right_rotate(e_val, 41)
            ch = (e_val & f_val) ^ (~e_val & g_val)
            temp1 = (h_val + S1 + ch + K[i] + w[i]) % (1 << 64)  # Using mod instead of add mod
            
            S0 = right_rotate(a_val, 28) ^ right_rotate(a_val, 34) ^ right_rotate(a_val, 39)
            maj = (a_val & b_val) ^ (a_val & c_val) ^ (b_val & c_val)
            temp2 = (S0 + maj) % (1 << 64)  # Using mod instead of add mod
            
            h_val = g_val
            g_val = f_val
            f_val = e_val
            e_val = (d_val + temp1) % (1 << 64)  # Using mod instead of add mod
            d_val = c_val
            c_val = b_val
            b_val = a_val
            a_val = (temp1 + temp2) % (1 << 64)  # Using mod instead of add mod
        
        # Update hash values for this block
        a = (a + a_val) % (1 << 64)  # Using mod instead of add mod
        b = (b + b_val) % (1 << 64)
        c = (c + c_val) % (1 << 64)
        d = (d + d_val) % (1 << 64)
        e = (e + e_val) % (1 << 64)
        f = (f + f_val) % (1 << 64)
        g = (g + g_val) % (1 << 64)
        h = (h + h_val) % (1 << 64)
        
        # Build the final hash for this block
        hash_values = [a, b, c, d, e, f, g, h]
        digest = ''.join(format(val, '016x').upper() for val in hash_values)
        
        # We're only keeping the first n_H_bits (512 bits = 64 bytes = 128 hex chars)
        digest = digest[:128]
        results.append(digest)
        
        # Verify against expected output
        if digest == expected_outputs[block_num]:
            print(f"Block {block_num+1}: Hash matches expected output!")
        else:
            print(f"Block {block_num+1}: Hash doesn't match expected output.")
            print(f"  Got:      {digest}")
            print(f"  Expected: {expected_outputs[block_num]}")
    
    return results

# The input message P from the problem
P = "5461C004A89C008312409C7914041C108174815B082C9B0212800D8507B905172412FD0D39E000D0842185B9038210353A36224BC9A88000060035B10DBC1F304C008042404119D8327010029B090023D11144A42201B05003839A0E182224291027080E62638A22806149121179416130029006A02404C0A11A009BBA046C00"

# Run the SHA-512 function on the input
result = sha512(P)

# Print all results
for i, digest in enumerate(result):
    print(f"Block {i+1}: {digest}")