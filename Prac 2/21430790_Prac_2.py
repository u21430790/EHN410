import numpy as np
import string


# ----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------


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
    print(des_Split_In_Two("E4600FA647F7C412"))

def test_RC4():
    key = "MyS3cr3tK3y#2025"
    print(rc4_Init_S_T(key))
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
    return


def des_Preprocess_String_Plaintext(plaintext: str) -> np.ndarray: # 2
    return


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
    k0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000eyPermChoice2 = np.load("DES_Arrays\\DES_Key_Permutation_Choice_2.npy")
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
    return


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
    print(K)
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
    return


def rc4_Process_Byte(byteToProcess: int, k: int) -> int: # 4
    return


def rc4_Encrypt_String(plaintext: str, key: str) -> np.ndarray: # 5
    return


def rc4_Decrypt_String(ciphertext: np.ndarray, key: str) -> str: # 6
    return


def rc4_Encrypt_Image(plaintext: np.ndarray, key: str) -> np.ndarray: # 7
    return


def rc4_Decrypt_Image(ciphertext: np.ndarray, key: str) -> np.ndarray: # 8
    return


# ----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------

#test_DES()
test_RC4()