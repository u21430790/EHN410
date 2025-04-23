import numpy as np
import string
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------

#print(ord('a')-36)
a = 2 
#print(a.encode('ascii').hex())
#print(f'{a:02X}')
'''
IMPORTANT!!
- Code submission due on Tuesday 29 April 2025, before 8h30, on AMS and ClickUP
- Prac test is two hours later at 10h30.
- Rename this file to <insertyourstudentnumberhere>_Prac_2.py
- submit .py on AMS, .pdf on ClickUP
- Comment your code (best practice)

- Use the function definitions given here/specified in the guide.
- DO NOT CHANGE THEM / USE DIFFERENT DATA TYPES!! For example, using lists instead of np.ndarrays

- Please read the practical guide for instructions.
- Unanswered questions? Email me (Miss Elna Fourie) at: u19049910@tuks.co.za
 
Changelog:
- 2024/04/17 --> replaced 'pass' with 'raise Exception()' for all functions
             --> For AES and DES Encrypt/Decrypt String/Image: load given *.npy arrays within functions
                    --> DO NOT CHANGE THE NP.LOAD() FUNCTIONS' FILE PATH, USE AS GIVEN
 
'''

def test_DES():
    #print(des_XOR('1A3F', 'B7C2'))
    #print(des_left_Shift('1A3F', 4))
    #print(des_Split_In_Two("E4600FA647F7C412"))
    plaintext = "abcdefgh"
    key = "12345678"
def test_RC4():
    """
    key = "MyS3cr3tK3y#2025"
    plaintext = "I am the one who meows"
    cipher = rc4_Encrypt_String(plaintext,key)
    print(cipher)
    decrypted = rc4_Decrypt_String(cipher,key)
    print(decrypted)
    """


    # Load image
    img = Image.open('jerry.png')
    img_np = np.array(img)
    image_dim = img_np.shape
    # Encrypt
    key = "ToonMouse2025"
    encrypted_img_np = rc4_Encrypt_Image(img_np, key)
    encrypted_img_np = encrypted_img_np.reshape(image_dim)
    Image.fromarray(encrypted_img_np).save('encrypted_jerry.png')

    # Decrypt
    decrypted_img_np = rc4_Decrypt_Image(encrypted_img_np, key)
    decrypted_img_np = decrypted_img_np.reshape(image_dim)
    Image.fromarray(decrypted_img_np).save('decrypted_jerry.png')

# ----------------------------------------------------------------------------------------------
# 3.1 AES Cipher
# ----------------------------------------------------------------------------------------------

def aes_Generate_Round_Keys(key: str, sBox: np.ndarray) -> np.ndarray: # 1
    return


def aes_Preprocess_String_Plaintext(plaintext: str) -> np.ndarray: # 2
    return


def aes_Create_Input_States(inputBytes: np.ndarray) -> np.ndarray: # 3
    return


def aes_remove_Padding(paddedArray: np.ndarray) -> np.ndarray: # 4
    return


def aes_Encrypt_String(plaintext: str, key: str) -> np.ndarray: # 5
    sBox = np.load("AES_Arrays\\AES_Sbox_lookup.npy")
    return


def aes_Decrypt_String(ciphertext: np.ndarray, key: str) -> str: # 6
    sBox = np.load("AES_Arrays\\AES_Sbox_lookup.npy")
    invsBox = np.load("AES_Arrays\\AES_Inverse_Sbox_lookup.npy")
    return


def aes_Preprocess_Image_Plaintext(plaintext: np.ndarray) -> np.ndarray: # 7
    return


def aes_Encrypt_Image(plaintext: np.ndarray, key: str) -> np.ndarray: # 8
    sBox = np.load("AES_Arrays\\AES_Sbox_lookup.npy")
    return


def aes_Decrypt_Image(ciphertext: np.ndarray, key: str) -> np.ndarray: # 9
    sBox = np.load("AES_Arrays\\AES_Sbox_lookup.npy")
    invsBox = np.load("AES_Arrays\\AES_Inverse_Sbox_lookup.npy")
    return


def aes_Add_Round_key(state: np.ndarray, roundKey: np.ndarray) -> np.ndarray: # 10
    return


def aes_Substitute_Bytes(state: np.ndarray, sBox: np.ndarray) -> np.ndarray: # 11
    return


def aes_Shift_Rows_Encrypt(state: np.ndarray) -> np.ndarray: # 12
    return


def aes_Shift_Rows_Decrypt(state: np.ndarray) -> np.ndarray: # 13
    return


def aes_Mix_Columns_Encrypt(state: np.ndarray) -> np.ndarray: # 14
    return


def aes_Mix_Columns_Decrypt(state: np.ndarray) -> np.ndarray: # 15
    return


def aes_Apply_Encryption_Round(state: np.ndarray, roundKey: np.ndarray, sBox: np.ndarray) -> np.ndarray: # 16
    return


def aes_Encrypt_State(state: np.ndarray, roundKeys: np.ndarray, sBox: np.ndarray) -> np.ndarray: # 17
    return


def aes_Apply_Decryption_Round(state: np.ndarray, roundKey: np.ndarray, sBox: np.ndarray) -> np.ndarray: # 18
    return


def aes_Decrypt_State(state: np.ndarray, roundKeys: np.ndarray, sBox: np.ndarray) -> np.ndarray: # 19
    return


def aes_des_rc4_Convert_To_Image(arrayToConvert: np.ndarray, originalShape: tuple) -> np.ndarray: # 20
    return


# ----------------------------------------------------------------------------------------------
# 3.2 DES Cipher
# ----------------------------------------------------------------------------------------------

def des_Generate_Round_Keys(key: str, permutedChoice1, permutedChoice2, roundShifts) -> np.ndarray: # 1
    keys = []

    #permed1 = des_Apply_Permutation(key,perm1,16)
    
    for shifts in roundShifts:
        shifted = des_left_Shift(permutedChoice1,shifts)
        keys.append(shifted)
    return np.array(keys)


def des_Preprocess_String_Plaintext(plaintext: str) -> np.ndarray: # 2
    plain_hex = np.array([])
    #print(a.encode('ascii').hex())
    #print(f'{a:02X}')
    for char in plaintext:
        plain_hex.append(char.encode('ascii').hex())
    if len(plain_hex)%8 != 0:
        pad_len = len(plain_hex)%8
        for i in range(pad_len):
            plain_hex.append(f'{pad_len:02x}')
    else: 
        for i in range(8):
            plain_hex.append('02')
    return plain_hex


def des_Create_Input_Blocks(processedArray: np.ndarray) -> np.ndarray: # 3
    return


def des_Remove_String_Padding(paddedArray: np.ndarray) -> np.ndarray: # 4
    return


def des_Encrypt_String(plaintext: str, key: str) -> np.ndarray: # 5
    keyPermChoice1 = np.load("DES_Arrays\\DES_Key_Permutation_Choice_1.npy")
    keyPermChoice2 = np.load("DES_Arrays\\DES_Key_Permutation_Choice_2.npy")
    keyRoundShifts = np.load("DES_Arrays\\DES_Round_Shifts.npy")
    sBoxes = np.load("DES_Arrays\\DES_sBoxes.npy")
    FexpansionBox = np.load("DES_Arrays\\DES_Expansion_Box.npy")
    FpermutationChoice = np.load("DES_Arrays\\DES_F_Function_Permutation.npy")
    initPerm = np.load("DES_Arrays\\DES_Initial_Permutation.npy")
    invInitPerm = np.load("DES_Arrays\\DES_Inverse_Initial_Permutation.npy")
    return


def des_Decrypt_String(ciphertext: np.ndarray, key: str) -> str: # 6
    keyPermChoice1 = np.load("DES_Arrays\\DES_Key_Permutation_Choice_1.npy")
    keyPermChoice2 = np.load("DES_Arrays\\DES_Key_Permutation_Choice_2.npy")
    keyRoundShifts = np.load("DES_Arrays\\DES_Round_Shifts.npy")
    sBoxes = np.load("DES_Arrays\\DES_sBoxes.npy")
    FexpansionBox = np.load("DES_Arrays\\DES_Expansion_Box.npy")
    FpermutationChoice = np.load("DES_Arrays\\DES_F_Function_Permutation.npy")
    initPerm = np.load("DES_Arrays\\DES_Initial_Permutation.npy")
    invInitPerm = np.load("DES_Arrays\\DES_Inverse_Initial_Permutation.npy")
    return


def des_Process_Block(block: str, roundKeys: np.ndarray, initialPerm: np.ndarray, sBoxes: np.ndarray,
                      expansionBox: np.ndarray, FpermChoice: np.ndarray, invInitialPerm: np.ndarray) -> str: # 7
    return


def des_Process_Round(roundInputValue: str, roundKey: str, sBoxes: np.ndarray, expansionBox: np.ndarray, 
                      permutationChoice: np.ndarray) -> str: # 8
    return


def des_Preprocess_Image_Plaintext(plaintext: np.ndarray) -> np.ndarray: # 9
    return


def des_Remove_Image_Padding(paddedArray: np.ndarray) -> np.ndarray: # 10
    return


def des_Encrypt_Image(plaintext: np.ndarray, key: str) -> np.ndarray: # 11
    keyPermChoice1 = np.load("DES_Arrays\\DES_Key_Permutation_Choice_1.npy")
    keyPermChoice2 = np.load("DES_Arrays\\DES_Key_Permutation_Choice_2.npy")
    keyRoundShifts = np.load("DES_Arrays\\DES_Round_Shifts.npy")
    sBoxes = np.load("DES_Arrays\\DES_sBoxes.npy")
    FexpansionBox = np.load("DES_Arrays\\DES_Expansion_Box.npy")
    FpermutationChoice = np.load("DES_Arrays\\DES_F_Function_Permutation.npy")
    initPerm = np.load("DES_Arrays\\DES_Initial_Permutation.npy")
    invInitPerm = np.load("DES_Arrays\\DES_Inverse_Initial_Permutation.npy")
    return


def des_Decrypt_Image(ciphertext: np.ndarray, key: str) -> np.ndarray: # 12
    keyPermChoice1 = np.load("DES_Arrays\\DES_Key_Permutation_Choice_1.npy")
    keyPermChoice2 = np.load("DES_Arrays\\DES_Key_Permutation_Choice_2.npy")
    keyRoundShifts = np.load("DES_Arrays\\DES_Round_Shifts.npy")
    sBoxes = np.load("DES_Arrays\\DES_sBoxes.npy")
    FexpansionBox = np.load("DES_Arrays\\DES_Expansion_Box.npy")
    FpermutationChoice = np.load("DES_Arrays\\DES_F_Function_Permutation.npy")
    initPerm = np.load("DES_Arrays\\DES_Initial_Permutation.npy")
    invInitPerm = np.load("DES_Arrays\\DES_Inverse_Initial_Permutation.npy")
    return


def des_Apply_Permutation(valueToPermute: str, permuteTable: np.ndarray, numBitsBeforePermute: int) -> str: # 13

    values_bin = list(bin(int(valueToPermute,16)))
    values_bin = values_bin[2:]
    values_bin = values_bin.zfill(numBitsBeforePermute)
    permed = np.empty(numBitsBeforePermute)
    for i in range(len(values_bin)):
        permed[permuteTable[i]] = values_bin[i]
    permuted_str = ''.join(permed)
    
    return f'{permuted_str:0X}'



def des_Split_In_Two(inputValue: str) -> np.ndarray: # 14
    length = len(inputValue)
    x1 = inputValue[0:length//2]
    x2 = inputValue[length//2:]

    return np.array([x1,x2])


def des_XOR(value1: str, value2: str) -> str: # 15
    length = max([len(value1),len(value2)])
    int1 = int(value1,16)
    int2 = int(value2,16)

    xored  = int1^int2

    return f'{xored:0{length}X}'


def des_left_Shift(inputValue: str, shiftCount: int) -> str: # 16
    int1 = int(inputValue,16)
    length = len(inputValue)*4
    bin_int1 = bin(int1)[2:]
  
    bin_int =bin_int1.zfill(length)
    
    bin_list = np.array(list(bin_int))
    bin_shifted = np.roll(bin_list,-shiftCount)

    bins = ''.join(bin_shifted)
    #print(bins)
    x = int(bins,2)

    return f'{x:04X}'


# ----------------------------------------------------------------------------------------------
# RC4 Stream Cipher
# ----------------------------------------------------------------------------------------------

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

    return cipher


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


def rc4_Encrypt_Image(plaintext: np.ndarray, key: str) -> np.ndarray:

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



# ----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------

test_DES()
#test_RC4()