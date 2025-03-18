import string
import numpy as np

def get_key(key:str):
    alph = list(string.ascii_lowercase)
    x=0
    new_key = ""
    while x<len(key):
        if key[x].lower() in alph and key[x].lower not in new_key:
            new_key+= key[x].lower()
        x+=1
    key_list = list(new_key)
    key_matrix = key_list

    y=0
    while len(key_matrix)<25:
        if alph[y] not in key_list and alph[y]!= "j":
            key_matrix.append((alph[y]))
        y+=1
    key_matrix = np.array(key_matrix)
    key_matrix = key_matrix.reshape(5,5)

    return key_matrix

def get_pos_in_key(val1,val2,keyMat):
    itemindex = np.where(keyMat == val)
    itemindex2 = np.where(keyMat == val2)
    return np.array([itemindex[0][0], itemindex[1][0], itemindex2[0][0], itemindex2[1][0]], dtype=int)

def get_encryption_pos(pos , keyMat):
    x_len = keyMat.shape[0]
    y_len = keyMat.shape[1]

    # Same row
    if pos[0] == pos[2]:
        pos[1] = pos[1]+1 if pos[1]<x_len -1 else 0
        pos[3] = pos[3]+1 if pos[3] <y_len-1 else 0
    
    # Same column
    if pos[1] == pos[3]:
        pos[0] = pos[0]+1 if pos[0]<x_len -1 else 0
        pos[2] = pos[2]+1 if pos[2] <y_len-1 else 0
    
    else:
        temp = pos[1]
        pos[1] = pos[3]
        pos[3] = temp
    
    return pos
def get_decryption_pos(pos: np.ndarray, keyMat: np.ndarray) -> np.ndarray: # 3.1.4
    x_len = keyMat.shape[0]
    y_len = keyMat.shape[1]
    # Both vals in same row
    if pos[0] == pos[2]:
        pos[1] = pos[1] -1 if pos[1]!=0 else x_len-1 
        pos[3] = pos[3]-1 if pos[3]!= 0 else x_len-1
        return pos
    # Both vals in same column
    if pos[1] == pos[3]:
        pos[0] = pos[0]-1 if pos[0]!=0 else y_len-1
        pos[2] = pos[2]-1 if pos[2]!=0 else y_len-1
        return pos
    else:
        temp = pos[1]
        pos[1] = pos[3]
        pos[3] = temp
       
    return pos

def preprocess_text(plaintext):
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

def playfair_encrypt_text(plaintext: str, key: str) -> str:
    
    new_text = preprocess_text(plaintext)
    key_matrix = get_key(True,key)
    cipher = ""
    # Encrypt every two characters
    for i in range(0,len(new_text),2):
        x = new_text[i]
        y = new_text[i+1]
        pos= get_pos_in_key(x,y,key_matrix)
        new_pos = get_encryption_pos(pos,key_matrix)
        cipher = cipher + key_matrix[new_pos[0]][new_pos[1]] + key_matrix[new_pos[2]][new_pos[3]]
    return cipher

def playfair_decrypt_text(ciphertext: str, key: str) -> str: 
    
    key_matrix = get_key(True,key)
    plaintext = ""
    # decrypt every two characters
    for i in range(0,len(ciphertext),2):
        x = ciphertext[i]
        y = ciphertext[i+1]
        pos= get_pos_in_key(x,y,key_matrix)
        new_pos = get_decryption_pos(pos,key_matrix)
        plaintext = plaintext + key_matrix[new_pos[0]][new_pos[1]] + key_matrix[new_pos[2]][new_pos[3]]
    
    x= 0 
    new_text = ""
    while x<len(plaintext):
        if plaintext[x]!= 'x':
            new_text = new_text+ plaintext[x]
        x+=1
    return new_text
