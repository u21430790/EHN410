def mod_pow(base, exponent, modulus):
    """
    Efficiently calculates (base^exponent) mod modulus using binary exponentiation
    """
    if modulus == 1:
        return 0
    result = 1
    base = base % modulus
    while exponent > 0:
        # If exponent is odd, multiply result with base
        if exponent % 2 == 1:
            result = (result * base) % modulus
        # Exponent = exponent / 2
        exponent = exponent >> 1
        # Base = base^2
        base = (base * base) % modulus
    return result

def rsa_encrypt(P_i, PU_b, n):
    """
    RSA encryption: C = (P_i)^PU_b mod n
    """
    C = [mod_pow(p, PU_b, n) for p in P_i]
    return C

def rsa_decrypt(C, PR_b, n):
    """
    RSA decryption: P_i = (C)^PR_b mod n
    """
    P_i = [mod_pow(c, PR_b, n) for c in C]
    return P_i

def blocks_to_hex(blocks):
    """
    Convert blocks to their hexadecimal representation
    """
    hex_string = ''.join([format(block, 'X') for block in blocks])
    return hex_string

# Given parameters
PR_b = 77
PU_b = 5
n = 119
n_blocks = 16
block_size = 5

# Original plaintext blocks
P_i = [16, 72, 18, 96, 2, 40, 12, 40, 4, 40, 8, 7, 10, 24, 96, 12]

# Encrypt the plaintext blocks
E = rsa_encrypt(P_i, PU_b, n)

# Decrypt the ciphertext blocks
P_i_ = rsa_decrypt(E, PR_b, n)

# Convert to hex representation
P_i_hex = blocks_to_hex(P_i)
E_hex = blocks_to_hex(E)
P_i__hex = blocks_to_hex(P_i_)

# Print results
print("Original plaintext blocks (P_i):")
print(" ".join(f"{p:5d}" for p in P_i))

print("\nEncrypted blocks (E):")
print(" ".join(f"{e:5d}" for e in E))

print("\nDecrypted blocks (P_i_):")
print(" ".join(f"{p:5d}" for p in P_i_))

print("\nHex representations:")
print(f"P_i (hex): {P_i_hex}")
print(f"E (hex):   {E_hex}")
print(f"P_i_ (hex): {P_i__hex}")

# Validate that our encryption/decryption matches the expected values
expected_E = [67, 4, 86, 10, 32, 24, 3, 24, 72, 24, 43, 28, 40, 96, 10, 3]

print("\nVerification:")
print(f"Our encryption matches expected: {E == expected_E}")
print(f"Original plaintext matches decrypted plaintext: {P_i == P_i_}")