# SHA ###########################################################################
#################################################################################
P3 = '819203119288A4D422987C04C9A2B421'

word1 = P3[:len(P3)//2]
word2 = P3[len(P3)//2:]
word1 = bin(int(word1,16))[2:].zfill(64)
word2 = bin(int(word2,16))[2:].zfill(64)

a = 0x6A
b= 0xBB
c = 0x3C
d = 0xA5

def process_round(a,b,c,d,word):
    
    c = b^c^d
    b = a^b
    a = a^int(word[:8],2)
    d = d^int(word[8:],2)
    return a,b,c,d

def process_block(a,b,c,d,full_word):
    blocks = []
    a_init = a
    b_init =b
    c_init =c
    d_init=d
    for i in range(0,len(full_word),16):
        blocks.append(full_word[i:i+16])
    counter =0
    for block in blocks:
        counter+=1
        a,b,c,d = process_round(a,b,c,d,block)
        abcd = f'{a:02X}'+ f'{b:02X}' + f'{c:02X}' + f'{d:02X}'
        print(f'round {counter} : {abcd}')
    a_f ,b_f,c_f,d_f = (a^a_init),(b^b_init),(c^c_init),(d^d_init)
    abcd_f  = f'{a_f:02X}'+ f'{b_f:02X}' + f'{c_f:02X}' + f'{d_f:02X}'
    print(f'H {abcd_f}')
    return a_f,b_f,c_f,d_f

a1,b1,c1,d1 = process_block(a,b,c,d,word1)
a2,b2,c2,d2 = process_block(a1,b1,c1,d1,word2)

#QUESTION 2 SIMPLE MAC ####################################################################################
###########################################################################################################
P2_MAC = 'D8A503441106B0C6501491275E172002400000309366C50A'
K2 = 0xC4C84A40
H =   '' #calculated hash code (hex)
MAC = '' #calculated MAC (hex)
AUTH = '' #'YES' or 'NO'

def simple_hash(message_blocks):
    
    hash_value = 0
    
    for block in message_blocks:
        
        block_int = int(block, 16)
        hash_value ^= block_int
    return f"{hash_value:08X}"

blocks = []
for i in range(0,len(P2_MAC)-8,8):
    blocks.append(P2_MAC[i:i+8])


x  = simple_hash(blocks)
#print(x) # '87A00297'  MATCHES
#print(encrypt(x,K2)) # 'C1E74500' MATCHES

# encrypted x != last 8 digits of P2_MAC

"""
#QUESTION 2
H_ans = '87A00297'   #[12]
MAC_ans = 'C1E74500' #[3]
AUTH_ans = 'NO' 	 #[5]
"""

# ANSI X9.17 EDE ROUNDS #############################################################################################
#####################################################################################################################
#QUESTION 1 [30]
V11= 'FBB36449' #(V1)
K11 = 0x141D2236 #(K1)
K21 = 0xE3BEDAD3 #(K2)
DT1 = ['1640227C','04220141','2E808817','26164484','81A6924D','E5121201','2093202C','84632D45']
DT1_hexint = [0x1640227C,0x04220141,0x2E808817,0x26164484,0x81A6924D,0xE5121201,0x2093202C,0x84632D45] #(DT1 to DT8)

X1 = [] #X1 to X8 (output of first EDE that takes DTi as input) [6]
R1 = [] #R1 to R8 [12] 
V1 = [] #V2 to V8    [12]
"""
MEMO 
#QUESTION 1 [30]
X1_ans = ['C1C2CC93', 'E2FFDEF1', '6BA9F453', 'A73AFCC5', '71F35B75', 'F1BF3FC1', 'C392FA40', 'CEFB5EB0'] #[6]
R1_ans = ['4B64E0A2', '6D3AF7A3', '42FB7B96', 'ECFA1192', '29D8A5C9', '5E87366E', '6C15F350', 'C85AFE86'] #[12]
V1_ans = ['CF8F5075', 'CAEC5516', '6C7BF381', '0EE99113', '1D0282F8', 'EA1175EB', 'EAAE7554', '4388DC72'] #[12]
"""
#Ri = EDE([K1, K2], [Vi ⊕ EDE([K1, K2], DTi)])
#Vi +1 = EDE([K1, K2], [Ri ⊕ EDE([K1, K2], DTi)])


def encrypt_round(input,key):
    left = input[:4]
    right = input[4:]
    new = right+left
    int_new = int(new,16)
     
    return f'{int_new^key:08X}'

def decrypt_round(input1,key): 
    xored =int(input1,16)^key
    xored_bin = f'{xored:08X}'

    left = xored_bin[:4]
    right = xored_bin[4:]
    new = right+left
     
    return new

for D in DT1:
    x  = encrypt_round(D,K11)
    x = decrypt_round(x,K21)
    x = encrypt_round(x,K11)
    X1.append(x)

seed = V11
for x in X1:
    R = f'{int(seed,16) ^ int(x,16):08X}'
    R = encrypt_round(R,K11)
    R = decrypt_round(R,K21)
    R= encrypt_round(R,K11)
    R1.append(R)
    seed =  f'{int(R,16) ^ int(x,16):08X}'
    seed = encrypt_round(seed,K11)
    seed = decrypt_round(seed,K21)
    seed= encrypt_round(seed,K11)
    V1.append(seed)

print(f'X1 : {X1}')
print(f'R1 : {R1}')
print(f'V1 : {V1}')
"""
MATCHES MEMO
X1 : ['C1C2CC93', 'E2FFDEF1', '6BA9F453', 'A73AFCC5', '71F35B75', 'F1BF3FC1', 'C392FA40', 'CEFB5EB0']
R1 : ['4B64E0A2', '6D3AF7A3', '42FB7B96', 'ECFA1192', '29D8A5C9', '5E87366E', '6C15F350', 'C85AFE86']
V1 : ['CF8F5075', 'CAEC5516', '6C7BF381', '0EE99113', '1D0282F8', 'EA1175EB', 'EAAE7554', '4388DC72']
"""


# RSA1##############################################################################################
####################################################################################################

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

# RSA2 ###########################################################################################
##################################################################################################
def mod_pow(base, exponent, modulus):
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
    C = [mod_pow(p, PU_b, n) for p in P_i]
    return C

def rsa_decrypt(C, PR_b, n):
    P_i = [mod_pow(c, PR_b, n) for c in C]
    return P_i

def blocks_to_hex(blocks):
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

# RC4 ###############################################################################
##################################################################################### 
# working 
import numpy as np

def rc4_Init_S_T(key) -> np.ndarray: # 1
    S = []
    T = []
    K = key
    keylen = len(key)
    for i in range(256):
        S.append(i)
        T.append(K[i % keylen ])

    return np.array([S,T])


def rc4_Init_Permute_S(sArray: np.ndarray, tArray: np.ndarray) -> np.ndarray: # 2
    j = 0
    for i in range(256):
        j = (j+ sArray[i] + tArray[i] ) % 256
        sArray[i],sArray[j]  = sArray[j], sArray[i]
    return sArray


def rc4_Generate_Stream_Iteration(i: int, j: int, sArray: np.ndarray) -> tuple: # 3

    i = (i+1) % 256
    j = (j+sArray[i]) % 256
    sArray[i], sArray[j] = sArray[j], sArray[i]
    t = (sArray[i] + sArray[j]) % 256
    k_stream = sArray[t]

    return (i,j,sArray,k_stream)


def rc4_Process_Byte(byteToProcess: int, k: int) -> int: # 4

    return byteToProcess^k


def rc4_Encrypt_String(plaintext, key) -> np.ndarray: # 5
    S_T = rc4_Init_S_T(key)
    S = S_T[0]
    T = S_T[1]
    permuted_S = rc4_Init_Permute_S(S,T)
    cipher = []
    i = 0
    j = 0
    for char in plaintext:
        i,j,permuted_S, k = rc4_Generate_Stream_Iteration(i,j,permuted_S)
        cipher.append(rc4_Process_Byte(char,k))

    return  ''.join(format(num, '02X') for num in cipher)


def rc4_Decrypt_String(ciphertext, key) -> str: # 6
    S_T = rc4_Init_S_T(key)
    S = S_T[0]
    T = S_T[1]
    permuted_S = rc4_Init_Permute_S(S,T)
    plaintext = []
    i = 0
    j = 0

    for byte in ciphertext:
        i,j,permuted_S, k = rc4_Generate_Stream_Iteration(i,j,permuted_S)
        plain_int = rc4_Process_Byte(byte,k)
        plaintext.append(plain_int)     
    
    return ''.join(format(num, '02X') for num in plaintext)


n_P_bits = 256
n_K_bits = 64
n_S_bits = 512
K = [163,84 ,  167,   191 ,  149,   189,    60 ,  187]

#Plaintext bytes (in HEX)
plaintext = "C010000B2A41061000618C28108081CB4445401B12CB1360594481C031A5809B"
plaintext_bytes = bytes.fromhex(plaintext)

#RC4 bytes (in HEX)
#rc4 = "FDE95DB23D5F81EE2822876BEE555584242A419A14D56583F7D33A504124BAAA"
#rc4_bytes = bytes.fromhex(rc4)
#print(f"plaintext to encrypt: {plaintext_bytes}")
#print(f"DEcrypt to decrypt: {plaintext_bytes}")
#Encrypt
#"3DF95DB9171E87FE28430B43FED5D44F606F0181061E76E3AE97BB9070813A31"
#Decrypt
#C010000B2A41061000618C28108081CB4445401B12CB1360594481C031A5809B

cipher = rc4_Encrypt_String(plaintext_bytes,K)
print(cipher)

print(rc4_Decrypt_String(bytes.fromhex(cipher),K))


### DIFFIE HELLMAN #################################################################
####################################################################################
K3_dec = [] #key (decimal/base 10)
K3_bin = '' #32-bit key (binary/base 2)
C3 = '385D1F04'
P3 = ''     #plaintext (hex)


q = 29
alpha = 11
Ya = 5
Yb = 12

def get_key(Ya, Yb, alpha, q):
    # get Xa
    Xa = -1
    for i in range(q):
        if pow(alpha,i) % q == Ya:
            Xa = i
            break
    
    # get the symmetric key
    return pow(Yb,Xa) % q

k = get_key(Ya,Yb, alpha, q)
#print(k)
k_bin = bin(k)[2:].zfill(8)
k_bin = k_bin*4
#print(k_bin)
k_hex =f'{int(k_bin,2):0X}'

plain = decrypt(C3,int(k_hex,16))
#################################################################################