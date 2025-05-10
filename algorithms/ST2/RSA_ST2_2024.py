

# Given parameters
pr_b = 23  # Bob's private key
pu_b = 7   # Bob's public key (not used in decryption but included for reference)
n_b = 187  # Modulus

C2 = '3A7C576D3C73A955'
def rsa_decrypt(cipher_blocks, d, n):
    return [f'{pow(c, d, n):02X}' for c in cipher_blocks]

cipher_blocks = [0x3A, 0x7C, 0x57, 0x6D, 0x3C, 0x73, 0xA9, 0x55]  
n = 187
d = 23
plaintext = rsa_decrypt(cipher_blocks, d, n)
print("Decrypted bytes:", plaintext)
#print("Decrypted ASCII:", ''.join(chr(x) for x in plaintext))


