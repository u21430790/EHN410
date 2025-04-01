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


# ----------------------------------------------------------------------------------------------
# 3.1 AES Cipher
# ----------------------------------------------------------------------------------------------

def aes_Generate_Round_Keys(key: str, sBox: np.ndarray) -> np.ndarray: # 1
    raise Exception("Not Implemented.")


def aes_Preprocess_String_Plaintext(plaintext: str) -> np.ndarray: # 2
    raise Exception("Not Implemented.")


def aes_Create_Input_States(inputBytes: np.ndarray) -> np.ndarray: # 3
    raise Exception("Not Implemented.")


def aes_remove_Padding(paddedArray: np.ndarray) -> np.ndarray: # 4
    raise Exception("Not Implemented.")


def aes_Encrypt_String(plaintext: str, key: str) -> np.ndarray: # 5
    sBox = np.load("AES_Arrays\\AES_Sbox_lookup.npy")
    raise Exception("Not Implemented.")


def aes_Decrypt_String(ciphertext: np.ndarray, key: str) -> str: # 6
    sBox = np.load("AES_Arrays\\AES_Sbox_lookup.npy")
    invsBox = np.load("AES_Arrays\\AES_Inverse_Sbox_lookup.npy")
    raise Exception("Not Implemented.")


def aes_Preprocess_Image_Plaintext(plaintext: np.ndarray) -> np.ndarray: # 7
    raise Exception("Not Implemented.")


def aes_Encrypt_Image(plaintext: np.ndarray, key: str) -> np.ndarray: # 8
    sBox = np.load("AES_Arrays\\AES_Sbox_lookup.npy")
    raise Exception("Not Implemented.")


def aes_Decrypt_Image(ciphertext: np.ndarray, key: str) -> np.ndarray: # 9
    sBox = np.load("AES_Arrays\\AES_Sbox_lookup.npy")
    invsBox = np.load("AES_Arrays\\AES_Inverse_Sbox_lookup.npy")
    raise Exception("Not Implemented.")


def aes_Add_Round_key(state: np.ndarray, roundKey: np.ndarray) -> np.ndarray: # 10
    raise Exception("Not Implemented.")


def aes_Substitute_Bytes(state: np.ndarray, sBox: np.ndarray) -> np.ndarray: # 11
    raise Exception("Not Implemented.")


def aes_Shift_Rows_Encrypt(state: np.ndarray) -> np.ndarray: # 12
    raise Exception("Not Implemented.")


def aes_Shift_Rows_Decrypt(state: np.ndarray) -> np.ndarray: # 13
    raise Exception("Not Implemented.")


def aes_Mix_Columns_Encrypt(state: np.ndarray) -> np.ndarray: # 14
    raise Exception("Not Implemented.")


def aes_Mix_Columns_Decrypt(state: np.ndarray) -> np.ndarray: # 15
    raise Exception("Not Implemented.")


def aes_Apply_Encryption_Round(state: np.ndarray, roundKey: np.ndarray, sBox: np.ndarray) -> np.ndarray: # 16
    raise Exception("Not Implemented.")


def aes_Encrypt_State(state: np.ndarray, roundKeys: np.ndarray, sBox: np.ndarray) -> np.ndarray: # 17
    raise Exception("Not Implemented.")


def aes_Apply_Decryption_Round(state: np.ndarray, roundKey: np.ndarray, sBox: np.ndarray) -> np.ndarray: # 18
    raise Exception("Not Implemented.")


def aes_Decrypt_State(state: np.ndarray, roundKeys: np.ndarray, sBox: np.ndarray) -> np.ndarray: # 19
    raise Exception("Not Implemented.")


def aes_des_rc4_Convert_To_Image(arrayToConvert: np.ndarray, originalShape: tuple) -> np.ndarray: # 20
    raise Exception("Not Implemented.")


# ----------------------------------------------------------------------------------------------
# 3.2 DES Cipher
# ----------------------------------------------------------------------------------------------

def des_Generate_Round_Keys(key: str, permutedChoice1, permutedChoice2, roundShifts) -> np.ndarray: # 1
    raise Exception("Not Implemented.")


def des_Preprocess_String_Plaintext(plaintext: str) -> np.ndarray: # 2
    raise Exception("Not Implemented.")


def des_Create_Input_Blocks(processedArray: np.ndarray) -> np.ndarray: # 3
    raise Exception("Not Implemented.")


def des_Remove_String_Padding(paddedArray: np.ndarray) -> np.ndarray: # 4
    raise Exception("Not Implemented.")


def des_Encrypt_String(plaintext: str, key: str) -> np.ndarray: # 5
    keyPermChoice1 = np.load("DES_Arrays\\DES_Key_Permutation_Choice_1.npy")
    keyPermChoice2 = np.load("DES_Arrays\\DES_Key_Permutation_Choice_2.npy")
    keyRoundShifts = np.load("DES_Arrays\\DES_Round_Shifts.npy")
    sBoxes = np.load("DES_Arrays\\DES_sBoxes.npy")
    FexpansionBox = np.load("DES_Arrays\\DES_Expansion_Box.npy")
    FpermutationChoice = np.load("DES_Arrays\\DES_F_Function_Permutation.npy")
    initPerm = np.load("DES_Arrays\\DES_Initial_Permutation.npy")
    invInitPerm = np.load("DES_Arrays\\DES_Inverse_Initial_Permutation.npy")
    raise Exception("Not Implemented.")


def des_Decrypt_String(ciphertext: np.ndarray, key: str) -> str: # 6
    keyPermChoice1 = np.load("DES_Arrays\\DES_Key_Permutation_Choice_1.npy")
    keyPermChoice2 = np.load("DES_Arrays\\DES_Key_Permutation_Choice_2.npy")
    keyRoundShifts = np.load("DES_Arrays\\DES_Round_Shifts.npy")
    sBoxes = np.load("DES_Arrays\\DES_sBoxes.npy")
    FexpansionBox = np.load("DES_Arrays\\DES_Expansion_Box.npy")
    FpermutationChoice = np.load("DES_Arrays\\DES_F_Function_Permutation.npy")
    initPerm = np.load("DES_Arrays\\DES_Initial_Permutation.npy")
    invInitPerm = np.load("DES_Arrays\\DES_Inverse_Initial_Permutation.npy")
    raise Exception("Not Implemented.")


def des_Process_Block(block: str, roundKeys: np.ndarray, initialPerm: np.ndarray, sBoxes: np.ndarray,
                      expansionBox: np.ndarray, FpermChoice: np.ndarray, invInitialPerm: np.ndarray) -> str: # 7
    raise Exception("Not Implemented.")


def des_Process_Round(roundInputValue: str, roundKey: str, sBoxes: np.ndarray, expansionBox: np.ndarray, 
                      permutationChoice: np.ndarray) -> str: # 8
    raise Exception("Not Implemented.")


def des_Preprocess_Image_Plaintext(plaintext: np.ndarray) -> np.ndarray: # 9
    raise Exception("Not Implemented.")


def des_Remove_Image_Padding(paddedArray: np.ndarray) -> np.ndarray: # 10
    raise Exception("Not Implemented.")


def des_Encrypt_Image(plaintext: np.ndarray, key: str) -> np.ndarray: # 11
    keyPermChoice1 = np.load("DES_Arrays\\DES_Key_Permutation_Choice_1.npy")
    keyPermChoice2 = np.load("DES_Arrays\\DES_Key_Permutation_Choice_2.npy")
    keyRoundShifts = np.load("DES_Arrays\\DES_Round_Shifts.npy")
    sBoxes = np.load("DES_Arrays\\DES_sBoxes.npy")
    FexpansionBox = np.load("DES_Arrays\\DES_Expansion_Box.npy")
    FpermutationChoice = np.load("DES_Arrays\\DES_F_Function_Permutation.npy")
    initPerm = np.load("DES_Arrays\\DES_Initial_Permutation.npy")
    invInitPerm = np.load("DES_Arrays\\DES_Inverse_Initial_Permutation.npy")
    raise Exception("Not Implemented.")


def des_Decrypt_Image(ciphertext: np.ndarray, key: str) -> np.ndarray: # 12
    keyPermChoice1 = np.load("DES_Arrays\\DES_Key_Permutation_Choice_1.npy")
    keyPermChoice2 = np.load("DES_Arrays\\DES_Key_Permutation_Choice_2.npy")
    keyRoundShifts = np.load("DES_Arrays\\DES_Round_Shifts.npy")
    sBoxes = np.load("DES_Arrays\\DES_sBoxes.npy")
    FexpansionBox = np.load("DES_Arrays\\DES_Expansion_Box.npy")
    FpermutationChoice = np.load("DES_Arrays\\DES_F_Function_Permutation.npy")
    initPerm = np.load("DES_Arrays\\DES_Initial_Permutation.npy")
    invInitPerm = np.load("DES_Arrays\\DES_Inverse_Initial_Permutation.npy")
    raise Exception("Not Implemented.")


def des_Apply_Permutation(valueToPermute: str, permuteTable: np.ndarray, numBitsBeforePermute: int) -> str: # 13
    raise Exception("Not Implemented.")


def des_Split_In_Two(inputValue: str) -> np.ndarray: # 14
    raise Exception("Not Implemented.")


def des_XOR(value1: str, value2: str) -> str: # 15
    raise Exception("Not Implemented.")


def des_left_Shift(inputValue: str, shiftCount: int) -> str: # 16
    raise Exception("Not Implemented.")


# ----------------------------------------------------------------------------------------------
# RC4 Stream Cipher
# ----------------------------------------------------------------------------------------------

def rc4_Init_S_T(key: str) -> np.ndarray: # 1
    raise Exception("Not Implemented.")


def rc4_Init_Permute_S(sArray: np.ndarray, tArray: np.ndarray) -> np.ndarray: # 2
    raise Exception("Not Implemented.")


def rc4_Generate_Stream_Iteration(i: int, j: int, sArray: np.ndarray) -> tuple: # 3
    raise Exception("Not Implemented.")


def rc4_Process_Byte(byteToProcess: int, k: int) -> int: # 4
    raise Exception("Not Implemented.")


def rc4_Encrypt_String(plaintext: str, key: str) -> np.ndarray: # 5
    raise Exception("Not Implemented.")


def rc4_Decrypt_String(ciphertext: np.ndarray, key: str) -> str: # 6
    raise Exception("Not Implemented.")


def rc4_Encrypt_Image(plaintext: np.ndarray, key: str) -> np.ndarray: # 7
    raise Exception("Not Implemented.")


def rc4_Decrypt_Image(ciphertext: np.ndarray, key: str) -> np.ndarray: # 8
    raise Exception("Not Implemented.")


# ----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------