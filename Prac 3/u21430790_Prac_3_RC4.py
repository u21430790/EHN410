import numpy as np

def rc4_Init_S_T(key: str) -> np.ndarray: # 1
    S = []
    T = []
    K = key.encode('ascii')
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


def rc4_Encrypt_String(plaintext: str, key: str) -> np.ndarray: # 5
    S_T = rc4_Init_S_T(key)
    S = S_T[0]
    T = S_T[1]
    permuted_S = rc4_Init_Permute_S(S,T)
    cipher = []
    i = 0
    j = 0
    for char in plaintext.encode('ascii'):
        i,j,permuted_S, k = rc4_Generate_Stream_Iteration(i,j,permuted_S)
        cipher.append(rc4_Process_Byte(char,k))

    return np.array(cipher)


def rc4_Decrypt_String(ciphertext: np.ndarray, key: str) -> str: # 6
    S_T = rc4_Init_S_T(key)
    S = S_T[0]
    T = S_T[1]
    permuted_S = rc4_Init_Permute_S(S,T)
    plaintext = ""
    i = 0
    j = 0
    for byte in ciphertext:
        i,j,permuted_S, k = rc4_Generate_Stream_Iteration(i,j,permuted_S)
        plain_int = rc4_Process_Byte(byte,k)

        plaintext += chr(plain_int)     
    
    return plaintext


def rc4_Encrypt_Image(plaintext: np.ndarray, key: str) -> np.ndarray: # 7

    flat = plaintext.flatten()
    
    # RC4 setup
    S_T = rc4_Init_S_T(key)
    S = S_T[0]
    T = S_T[1]
    permuted_S = rc4_Init_Permute_S(S, T)
    
    ciphertext = np.zeros_like(flat, dtype=np.uint8)
    i = j = 0
    for idx in range(len(flat)):
        i, j, permuted_S, k = rc4_Generate_Stream_Iteration(i, j, permuted_S)
        ciphertext[idx] = rc4_Process_Byte(flat[idx], k)
    
    return ciphertext


def rc4_Decrypt_Image(ciphertext: np.ndarray, key: str) -> np.ndarray:
    return rc4_Encrypt_Image(ciphertext, key)
