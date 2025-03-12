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
from PIL import Image
import matplotlib.pyplot as plt

# 3.1 Playfair Cipher
# ----------------------------------------------------------------------------------------------------
def test():
    # PLAYFAIR
    
    # key = "monarchy"
    # key_m = playfair_get_key(True,key)
    # #print(key_m)
    # x = playfair_get_pos_in_key("h","s",key_m)
    # #print(x)
    # #print(playfair_get_encryption_pos(x,key_m))
    # y = playfair_encrypt_text("balloon",key)
    # print(y)
    # z = playfair_decrypt_text(y,key)
    # print(z)

    # HILL

    #key = hill_get_key(True,"abcd")
    #vals = hill_pre_process_text("abcd",9)
    #print(key)
    #print(vals)
#     image_path = "emoji.jpg"  # Replace with your image path
#     img = Image.open(image_path)
#     img_array = np.array(img)

# # Display the original image
#     plt.figure(figsize=(10, 4))
#     plt.subplot(1, 3, 1)
#     plt.imshow(img_array)
#     plt.title("Original Image")

# # Encrypt the image
#     key = "secretkey123"
#     encrypted = playfair_encrypt_image(img_array, key)

# # Display the encrypted data (reshaped for visualization)
#     encrypted_img = playfair_convert_to_image(encrypted, img_array.shape)
#     plt.subplot(1, 3, 2)
#     plt.imshow(encrypted_img)
#     plt.title("Encrypted Image")

# # Decrypt the image
#     decrypted = playfair_decrypt_image(True, encrypted, key)
#     decrypted_img = playfair_convert_to_image(decrypted, img_array.shape)

# # Display the decrypted image
#     plt.subplot(1, 3, 3)
#     plt.imshow(decrypted_img)
#     plt.title("Decrypted Image")

#     plt.tight_layout()
#     plt.show()

# # Compare the original and decrypted images
#     differences = np.sum(img_array != decrypted_img)
#     print(f"Number of different pixels: {differences}")
#     print(f"Percentage difference: {differences / img_array.size * 100:.4f}%")



    key = "azAZ!@12"
    plaintext = "attackpostponeduntiltwoam"
    x =row_gen_key(key)
    print(x)

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
        unique_chars = []
        for char in key:
            if char not in unique_chars:
                unique_chars.append(char)
        
        ascii_values = [ord(char) % 256 for char in unique_chars]
        

        all_values = list(range(256))
        for val in ascii_values:
            if val in all_values:
                all_values.remove(val)
    
        key_values = ascii_values + all_values

        key_matrix = np.array(key_values).reshape(16, 16)
        
        return key_matrix
    
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
    #new_text = playfair_preprocess_text(ciphertext)
    key_matrix = playfair_get_key(True,key)
    plaintext = ""
    for i in range(0,len(ciphertext),2):
        x = ciphertext[i]
        y = ciphertext[i+1]
        pos= playfair_get_pos_in_key(x,y,key_matrix)
        new_pos = playfair_get_decryption_pos(pos,key_matrix)
        plaintext = plaintext + key_matrix[new_pos[0]][new_pos[1]] + key_matrix[new_pos[2]][new_pos[3]]
    
    x= 0 
    new_text = ""
    while x<len(plaintext):
        if plaintext[x]!= 'x':
            new_text = new_text+ plaintext[x]
        x+=1
    return new_text

def playfair_preprocess_image(plaintext: np.ndarray) -> np.ndarray: # 3.1.8
    flattened = plaintext.flatten()
    flattened = np.where(flattened == 129, 128, flattened)
    
    if len(flattened) % 2 != 0:
        flattened = np.append(flattened, 129)
    
    return flattened

def playfair_remove_image_padding(plaintextWithPadding: np.ndarray) -> np.ndarray: # 3.1.9
    new_text = []
    for i in range(len(plaintextWithPadding)):
        if plaintextWithPadding[i] != 129:
            new_text.append(plaintextWithPadding[i])
    return np.array(new_text)

def playfair_encrypt_image(plaintext: np.ndarray, key: str) -> np.ndarray: # 3.1.10
    processed_image = playfair_preprocess_image(plaintext)    
    key_matrix = playfair_get_key(False, key)

    ciphertext = np.zeros_like(processed_image)
    for i in range(0, len(processed_image), 2):
        if i+1 < len(processed_image):  
            x = processed_image[i]
            y = processed_image[i+1]
            
            pos = playfair_get_pos_in_key(x, y, key_matrix)

            new_pos = playfair_get_encryption_pos(pos, key_matrix)
            ciphertext[i] = key_matrix[new_pos[0]][new_pos[1]]
            ciphertext[i+1] = key_matrix[new_pos[2]][new_pos[3]]
    
    return ciphertext

def playfair_decrypt_image(removePadding: bool, ciphertext: np.ndarray, key: str) -> np.ndarray: # 3.1.11
    key_matrix = playfair_get_key(False, key)   
    plaintext = np.zeros_like(ciphertext)
    
    for i in range(0, len(ciphertext), 2):
        if i+1 < len(ciphertext):  
            x = ciphertext[i]
            y = ciphertext[i+1]

            pos = playfair_get_pos_in_key(x, y, key_matrix)
            new_pos = playfair_get_decryption_pos(pos, key_matrix)
            plaintext[i] = key_matrix[new_pos[0]][new_pos[1]]
            plaintext[i+1] = key_matrix[new_pos[2]][new_pos[3]]
    
    if removePadding:
        plaintext = playfair_remove_image_padding(plaintext)
    
    return plaintext

def playfair_convert_to_image(imageData: np.ndarray, originalShape) -> np.ndarray: # 3.1.12

    required_size = originalShape[0] * originalShape[1] * originalShape[2]
    if len(imageData) < required_size:
        padding_needed = required_size - len(imageData)
        padded_data = np.pad(imageData, (0, padding_needed), 'constant', constant_values=0)
        reshaped_image = padded_data.reshape(originalShape)
    elif len(imageData) > required_size:
        reshaped_image = imageData[:required_size].reshape(originalShape)
    else:
        reshaped_image = imageData.reshape(originalShape)
    
    return reshaped_image

# ----------------------------------------------------------------------------------------------------

# 3.2 Hill Cipher
# ----------------------------------------------------------------------------------------------------

def hill_get_key(isText:bool, key: str) -> np.ndarray: # 3.2.1
    if isText:
        key_list = list(key)
        for i in range(len(key_list)):
            key_list[i] = ord(key_list[i]) % 97
        #print(key_list)
        key_list  = np.array(key_list)
        if len(key_list) == 4:
            key_list = key_list.reshape(2,2)
        if len(key_list) == 9:
            key_list = key_list.reshape(3,3)

        det = np.linalg.det(key_list)
        #print(det)
        if det == 0:
            for i in range(key_list.shape[0]):
                for j in range(key_list.shape[1]):
                    key_list[i][j] = -1
        return key_list
    else:
        return

def hill_get_inv_key(isText: bool, keyMat: np.ndarray) -> np.ndarray: # 3.2.2
    if isText:
        # For text, modulo is 26
        modulus = 26
    else:
        # For images, modulo is 256
        modulus = 256
    
    # Get the size of the matrix
    n = keyMat.shape[0]
    
    # Calculate the determinant
    det = int(round(np.linalg.det(keyMat))) % modulus
    
    # Find modular multiplicative inverse of determinant
    det_inv = None
    for i in range(1, modulus):
        if (det * i) % modulus == 1:
            det_inv = i
            break
    
    if det_inv is None:
        # Return a matrix of -1 if inverse doesn't exist
        return np.full(keyMat.shape, -1)
    
    # Calculate the adjugate matrix
    if n == 2:
        adj = np.array([
            [keyMat[1, 1], -keyMat[0, 1]],
            [-keyMat[1, 0], keyMat[0, 0]]
        ])
    else:  # n == 3
        adj = np.zeros((3, 3), dtype=int)
        for i in range(3):
            for j in range(3):
                # Get the minor by excluding row i and column j
                minor = np.delete(np.delete(keyMat, i, axis=0), j, axis=1)
                # Calculate the cofactor
                cofactor = int(round(np.linalg.det(minor))) * (-1)**(i+j)
                # Store in adjugate (transpose of cofactor matrix)
                adj[j, i] = cofactor % modulus
    
    # Calculate the inverse: (det_inv * adj) % modulus
    inv_key = (det_inv * adj) % modulus
    
    return inv_key

def hill_process_group(isText: bool, group: np.ndarray, keyMat: np.ndarray) -> np.ndarray: # 3.2.3
    if isText:
        result = np.dot(keyMat, group) % 26
        return result
    else:
        result = np.dot(keyMat, group) % 256
        return result

def hill_pre_process_text(plaintext: str, keyLength: int) -> np.ndarray: # 3.2.4
    alph = list(string.ascii_lowercase)
    new_text =[]
    for s in plaintext:
        if s.lower() in alph:
            new_text.append(s.lower())
    if keyLength == 4:
        while len(new_text) % 2 !=0:
            new_text.append("x")
    if keyLength == 9:
        while len(new_text) % 3 !=0:
            new_text.append("x")
    
    for i in range(len(new_text)):
        new_text[i] = ord(new_text[i]) % 97
    
    return np.array(new_text)

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
    ascii_key = []
    new_key = []
    key_matrix = []
    for x in key:
        if x not in new_key:
            new_key.append(x)

    for i in new_key:
        ascii_key.append(ord(i))

    sorted_ascii = list(ascii_key)
    sorted_ascii.sort()
    for i in sorted_ascii:
        key_matrix.append(ascii_key.index(i))
    return np.array(key_matrix)

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