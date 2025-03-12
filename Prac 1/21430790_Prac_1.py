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
    key_m = playfair_get_key(True,key)
    #print(key_m)
    x = playfair_get_pos_in_key("h","s",key_m)
    #print(x)
    #print(playfair_get_encryption_pos(x,key_m))
    y = playfair_encrypt_text("balloon",key)
    print(y)
##############################################################################################################

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

        return  key_matrix
    else:
        return
    
def playfair_get_pos_in_key(val, val2, keyMat: np.ndarray) -> np.ndarray: # 3.1.2
    x_val_1 =-1
    y_val_1 = -1
    x_val_2= -1
    y_val_2 = -1

    for i in range(keyMat.shape[0]):
        for j in range(keyMat.shape[1]):
            if val == keyMat[i][j]:
                x_val_1 = i
                y_val_1 = j
            if val2 == keyMat[i][j]:
                x_val_2 = i
                y_val_2 = j
    pos = np.array([x_val_1,y_val_1,x_val_2,y_val_2])
    return pos

def playfair_get_encryption_pos(pos: np.ndarray, keyMat: np.ndarray) -> np.ndarray: # 3.1.3
    x_len = keyMat.shape[0]
    y_len = keyMat.shape[1]

    if pos[0] == pos[2]:
        pos[1] = pos[1] + 1 if pos[1] < x_len - 1 else 0
        pos[3] = pos[3] +1 if pos[3]< x_len-1 else 0
        return pos
    
    if pos[1] == pos[3]:
        pos[0] = pos[0] +1 if pos[0]<y_len-1 else 0 
        pos[2] =pos[2]+1 if pos[2]< y_len-1 else 0
        return pos
    else:
        temp = pos[1]
        pos[1] = pos[3]
        pos[3] = temp
        return pos

def playfair_get_decryption_pos(pos: np.ndarray, keyMat: np.ndarray) -> np.ndarray: # 3.1.4
    x_len = keyMat.shape[0]
    y_len = keyMat.shape[1]

    if pos[0] == pos[2]:
        pos[1] = pos[1] -1 if pos[1]!=0 else x_len-1 
        pos[3] = pos[3]-1 if pos[3]!= 0 else x_len-1
        return pos
    
    if pos[1] == pos[3]:
        pos[0] = pos[0]-1 if pos[0]!=0 else y_len-1
        pos[2] = pos[2]-1 if pos[2]!=0 else y_len-1
        return pos
    else:
        temp = pos[1]
        pos[1] = pos[3]
        pos[3] = temp
        return pos

def playfair_preprocess_text(plaintext: str) -> str: # 3.1.5
    alph = list(string.ascii_lowercase)
    x=0
    new_text = ""
    while x<len(plaintext):
        if plaintext[x].lower() in alph:
            if plaintext[x].lower() == "j":
                    new_text+= "i"
            else:
                    new_text+=plaintext[x].lower()
                    
        x+=1
    y = 0
    while y<len(new_text)-2:
        x1 = new_text[y]
        x2 = new_text[y+1]
        
        if x1 == x2:
            new_text = new_text[:y+1]+'x' +new_text[y+1:]
            y+=2
        
        else:
            y+=2
    if len(new_text) % 2 !=0:
        new_text = new_text+ 'x'
    return new_text

def playfair_encrypt_text(plaintext: str, key: str) -> str: # 3.1.6
    new_text = playfair_preprocess_text(plaintext)
    key_matrix = playfair_get_key(True,key)
    cipher = ""
    for i in range(0,len(new_text),2):
        x = new_text[i]
        y = new_text[i+1]
        pos= playfair_get_pos_in_key(x,y,key_matrix)
        new_pos = playfair_get_encryption_pos(pos,key_matrix)
        cipher = cipher + key_matrix[new_pos[0]][new_pos[1]] + key_matrix[new_pos[2]][new_pos[3]]
    return cipher

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