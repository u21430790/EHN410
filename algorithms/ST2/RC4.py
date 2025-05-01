# working 
import numpy as np

def rc4_Init_S_T(key) -> np.ndarray: # 1
    S = []
    T = []
    K = key
    keylen = len(key)
    for i in range(512):
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


print(rc4_Decrypt_String(bytes.fromhex(cipher),K))