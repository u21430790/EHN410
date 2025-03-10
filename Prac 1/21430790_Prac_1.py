# Name: Alexandros Theodorou    
# Student num: 21430790

'''
IMPORTANT!!

- Due 13 March 2024 (before 8h30) 
- No late submissions (AMS and Turnitin) accepted after 8h30!
- The prac test starts at 10h30 in the Netlabs.

- Rename this file to "<YourStudentNumber>_Prac_1.py", for example: "19056789_Prac_1.py"
- Comment your code (follow best practice)
- Submit .py to AMS and a .pdf to ClickUp (TurnItIn)
- Also, please upload your turnitin receipt to the AMS.
- Remove all print statements - and helper functions (that weren't provided) - used for unit testing.

- Please read the practical guide for instructions!
'''

import string
import numpy as np


# 3.1 Playfair Cipher
# ----------------------------------------------------------------------------------------------------
def test():
    key = "monarchy"
    playfair_get_key(True,key)

def playfair_get_key(isText: bool, key: str) -> np.ndarray: # 3.1.1
    if isText:
        alph = list(string.ascii_lowercase)
        x=0
        new_key = ""
        while x<len(key):
            if key[x].lower() in alph and key[x].lower() not in new_key:
                new_key+=key[x].lower()
            x+=1
        key_list = list(new_key)
        key_matrix = key_list
        
        y=0
        while len(key_matrix)<25:
            if alph[y] not in key_list and alph[y]!= "j":
                key_matrix.append(alph[y])
            y+=1
        key_matrix = np.array(key_matrix)
        key_matrix= key_matrix.reshape(5,5)
        print(key_matrix)
        return 
    else:
        return
    
def playfair_get_pos_in_key(val, val2, keyMat: np.ndarray) -> np.ndarray: # 3.1.2
    return

def playfair_get_encryption_pos(pos: np.ndarray, keyMat: np.ndarray) -> np.ndarray: # 3.1.3
    return

def playfair_get_decryption_pos(pos: np.ndarray, keyMat: np.ndarray) -> np.ndarray: # 3.1.4
    return

def playfair_preprocess_text(plaintext: str) -> str: # 3.1.5
    return

def playfair_encrypt_text(plaintext: str, key: str) -> str: # 3.1.6
    return

def playfair_decrypt_text(ciphertext: str, key: str) -> str: # 3.1.7
    return

def playfair_preprocess_image(plaintext: np.ndarray) -> np.ndarray: # 3.1.8
    return

def playfair_remove_image_padding(plaintextWithPadding: np.ndarray) -> np.ndarray: # 3.1.9
    return

def playfair_encrypt_image(plaintext: np.ndarray, key: str) -> np.ndarray: # 3.1.10
    return

def playfair_decrypt_image(removePadding: bool, ciphertext: np.ndarray, key: str) -> np.ndarray: # 3.1.11
    return

def playfair_convert_to_image(imageData: np.ndarray, originalShape) -> np.ndarray: # 3.1.12
    return

# ----------------------------------------------------------------------------------------------------

# 3.2 Hill Cipher
# ----------------------------------------------------------------------------------------------------

def hill_get_key(isText:bool, key: str) -> np.ndarray: # 3.2.1
    return

def hill_get_inv_key(isText: bool, keyMat: np.ndarray) -> np.ndarray: # 3.2.2
    return

def hill_process_group(isText: bool, group: np.ndarray, keyMat: np.ndarray) -> np.ndarray: # 3.2.3
    return

def hill_pre_process_text(plaintext: str, keyLength: int) -> np.ndarray: # 3.2.4
    return

def hill_encrypt_text(plaintext: str, key: str) -> str: # 3.2.5
    return

def hill_decrypt_text(ciphertext: str, key: str) -> str: # 3.2.6
    return

def hill_pre_process_image(plaintext: np.ndarray, keyLength: int) -> np.ndarray: # 3.2.7
    return

def hill_encrypt_image(plaintext: np.ndarray, key: str) -> np.ndarray: # 3.2.8
    return

def hill_decrypt_image(ciphertext: np.ndarray, key: str) -> np.ndarray: # 3.2.9
    return

def hill_convert_to_image(imageData: np.ndarray, originalShape) -> np.ndarray: # 3.2.10
    return

# ----------------------------------------------------------------------------------------------------

# 3.3 Row Transposition Cipher
# ----------------------------------------------------------------------------------------------------

def row_gen_key(key: str) -> np.ndarray: # 3.3.1
    return

def row_pad_text(plaintext: str, key: np.ndarray) -> str: # 3.3.2
    return

def row_encrypt_single_stage(plaintext: str, key: np.ndarray) -> str: # 3.3.3
    return

def row_decrypt_single_stage(ciphertext: str, key: np.ndarray) -> str: # 3.3.4
    return

def row_encrypt(plaintext: str, key: str, stage: int) -> str: # 3.3.5
    return

def row_decrypt(ciphertext: str, key: str, stage: int) -> str: # 3.3.6
    return

# ----------------------------------------------------------------------------------------------------
test()