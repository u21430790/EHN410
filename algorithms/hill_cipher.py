import numpy as np

def hill_get_key(isText:bool, key: str) -> np.ndarray: 
    '''
    * Get the hill key matrix (size 2x2 or 3x3)
    * You may assume that the text key is the correct length and has been pre-processed.
    '''
    key_matrix = []
    for i in key:
        key_matrix.append(ord(i.lower())-97)
    key_matrix = np.array(key_matrix)
    if len(key)== 4:
        key_matrix = key_matrix.reshape(2,2)
    if len(key)== 9:
        key_matrix =key_matrix.reshape(3,3)

    return key_matrix

# ---------------------------------------------------------------------------------------------------
def hill_process_group(isText: bool, group: np.ndarray, keyMat: np.ndarray) -> np.ndarray: 
    '''
    * Group size will be 2 or 3
    * This function receives a group of numbers (with the group size being the size required by the key) and multiplies (and mods) the group with the key.
    * The result is returned as a 1D ndarray with the same size as the group.
    '''
    return np.matmul(group,keyMat) % 26

# ---------------------------------------------------------------------------------------------------
def hill_pre_process_text(plaintext: str, keyLength: int) -> np.ndarray: 
    '''
    * This function receives a string message (plaintext) and removes all special characters and numbers and changes uppercase letters to lowercase.
    * Use the padding value "x" if needed.
    * The string is converted into a 1D ndarray of integers representing the characters (a = 0 . . . z = 25).
    '''
    text = []
    meow = []
    alph = 'abcdefghijklmnopqrstuvwxyz'
    for p in plaintext:
        if p.lower() in alph:
            text.append(p.lower())
    
    x= 0 
    while len(text) % keyLength !=0:
        x+=1
        text+= 'x'
    #print(plaintext)
    for f in text:
        meow.append(ord(f)-97)
        
    return np.array(meow)

# ---------------------------------------------------------------------------------------------------
def hill_encrypt_text(plaintext: str, key: str) -> str: 
    '''
    * Encrypts the plaintext message using the key supplied and the Hill cipher algorithm.
    '''
    
    key_mat= hill_get_key(True, key)
    key_length = len(key_mat)
    meow = []
    meow2= ''
    text = hill_pre_process_text(plaintext, key_length)
    #print(text)
    for i in range(0,len(text),key_length):
        #print(i)
        group = text[i:i+key_length]
        #(group)
        x= hill_process_group(True, group, key_mat)
        #print(x)
        meow.extend(x)
    for m in meow:
        meow2+= chr(m + 97)
    return meow2
    