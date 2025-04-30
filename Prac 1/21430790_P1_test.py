import numpy as np
import string

# Q1 - PF Decrypt
# ===============================================================================
'''
Key = "Life is like a box of chocolates."
Plaintext = ?
Ciphertext = "lndxravhnkolnankqasbesngldhvgpsezlso"
'''
# ===============================================================================

def testPf():
    Key = "Life is like a box of chocolates."
    Ciphertext = "lndxravhnkolnankqasbesngldhvgpsezlso"
    key = playfair_get_key(True, Key)
    print(key)
    x = playfair_decrypt_text(Ciphertext, Key)
    print(x)
    return

def testhill():
    Key = "fbwupesaj"
    Plaintext = "Lorem ipsum dolor sit amet" 
    s = hill_encrypt_text(Plaintext, Key)
    print(s)
    return

def testRow():
    Key = "Hello123!"
    key2 ="azAZ!@12"
    Ciphertext_2 = "eexvnpxneguinxaoouxyvrxg"
    #print(row_gen_key(Key))
    x = row_decrypt(Ciphertext_2, Key,2)
    print(x)
    return
# ---------------------------------------------------------------------------------------------------
def playfair_get_key(isText: bool, key: str) -> np.ndarray: 
    '''
    * Returns the key matrix that will be used during decryption as 2D ndarray with type String.
    * Capital letters should be changed to lowercase letters.
    * Remove duplicate values, special characters and numbers from key.
    * Replace ‘j’ with ‘i’.
    * Only uses the lowercase English alphabet (‘a’ – ‘z’, excluding ‘j’).
    '''
    alph = 'abcdefghijklmnopqrstuvwxyz'
    #alph = list(string.ascii_lowercase())
    key_matrix = []
    for i in key:
        if i.lower() in alph and i not in key_matrix:
            if i.lower() == "j":
                key_matrix.append(i)
            else:
                key_matrix.append(i.lower())
    #print(key_matrix)
    x=0
    while len(key_matrix)<25:
        if alph[x] not in key_matrix and alph[x] != "j" :
            key_matrix.append(alph[x])
        x+=1    
    key_matrix = np.array(key_matrix)
    key_matrix =key_matrix.reshape(5,5)
    
    return key_matrix
# ---------------------------------------------------------------------------------------------------    
def playfair_get_pos_in_key(val, val2, keyMat: np.ndarray) -> np.ndarray: 
    itemindex = np.where(keyMat == val)
    itemindex2 = np.where(keyMat == val2)
    return np.array([itemindex[0][0], itemindex[1][0], itemindex2[0][0], itemindex2[1][0]], dtype=int)

# ---------------------------------------------------------------------------------------------------
def playfair_get_decryption_pos(pos: np.ndarray, keyMat: np.ndarray) -> np.ndarray: 
    '''
    * pos is the ndarray returned by playfair_get_pos_in_key.
    * This function applies the encryption rules of the Playfair cipher and returns a 1D ndarray with the same format as playfair_get_pos_in_key with the updated positions.
    '''
    if pos[0] == pos[2]:
        pos[1] = pos[1]-1 if pos[1] !=0 else 4
        pos[3] = pos[3]-1 if pos[3] !=0 else 4
    if pos[1] == pos[3]:
        pos[0] = pos[0]-1 if pos[0] !=0 else 4
        pos[2] = pos[2]-1 if pos[2] !=0 else 4            
    
    else:
        temp = pos[1]
        pos[1] = pos[3]
        pos[3] = temp
    return np.array(pos)

# ---------------------------------------------------------------------------------------------------
def playfair_preprocess_text(plaintext: str) -> str: 
    '''
    * This function changes uppercase letters to lowercase letters and removes special characters and numbers.
    * Replace 'j' with 'i'.
    * This function also adds padding and filler values to the plaintext as required. Use ‘x’ for this purpose.
    '''
    alph = 'abcdefghijklmnopqrstuvwxyz'
    new_text = ""
    for i in plaintext:
        if i.lower() in alph:
            if i.lower() == "j":
                new_text+= "i"
            else:
                new_text+= i.lower()
    x = 0
    
    while x< len(new_text)-2:
        x1 = new_text[x]
        x2 = new_text[x+1]
        if x1 == x2:
            new_text = new_text[:x+1] +'x'+new_text[x+1:]
        x+=2
    if len(new_text)%2 !=0:
        new_text+= 'x'
    
    return new_text
# ---------------------------------------------------------------------------------------------------
def playfair_decrypt_text(ciphertext: str, key: str) -> str: 
    '''
    * This function applies the Playfair decryption cipher to the supplied string plaintext using the key.
    '''
    plaintext = ""
    text = ""
    keyMat = playfair_get_key(True,key)
    for i in range(0,len(ciphertext),2):
        x1 = ciphertext[i]
        x2 = ciphertext[i+1]
        
        pos= playfair_get_pos_in_key(x1, x2, keyMat)
        new_pos = playfair_get_decryption_pos(pos, keyMat)
        plaintext+= keyMat[pos[0]][pos[1]] + keyMat[pos[2]][pos[3]]
    for p in plaintext:
        if p!= 'x':
            text+=p
    return text

# ===============================================================================



# Q2 - Hill Encrypt
# ===============================================================================
'''
Key = "fbwupesaj"
Plaintext = "Lorem ipsum dolor sit amet" 
Ciphertext = ?
'''
# ===============================================================================

# ---------------------------------------------------------------------------------------------------
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
        group = text[i:i+key_length]

        x= hill_process_group(True, group, key_mat)

        meow.extend(x)
    for m in meow:
        meow2+= chr(m + 97)
    return meow2
# ===============================================================================



# Q3 - Row Transposition Cipher Decrypt two stages
# ===============================================================================
'''
Key = "Hello123!"
Plaintext = ?
Ciphertext_1 = ?
Ciphertext_2 = "eexvnpxneguinxaoouxyvrxg"
'''
# ===============================================================================

# ---------------------------------------------------------------------------------------------------
def row_gen_key(key: str) -> np.ndarray: 
    '''
    item This function converts the key into a list that contains the order of the indices to use during encryption.
    item Duplicate values in the key should be removed.
    item Example: Input key “azAZ!@12” should return [4 6 7 5 2 3 0 1].
    item The output array contains, in order, the indices in the key that need to be used. To clarify:}
    The ASCII values for the key in the example (azAZ!@12):
    a - 97
    z - 122
    A - 65
    Z - 90
    ! - 33
    @ - 64
    1 - 49
    2 - 50
    From these, the lowest number is 33, the ‘!’. The position of ‘!’ in the original key in index 4. The second smallest number is 49, the ‘1’. The position of the ‘1’ in the key is index 6. The highest number is 122, the ‘z’. The position of ‘z’ in the key is index 1.
    This is how the output of [4 6 7 5 2 3 0 1] is found. This means that the first column to use during encryption is the 4th column, the second is the 6th, and so on.
    '''
    key_matrix = []
    ascii_matrix = []
    temp_matrix = []
    for x in key:
        if x not in temp_matrix:
            temp_matrix.append(x)
    #print(temp_matrix)       
    for i in temp_matrix:
        ascii_matrix.append(ord(i))
    
    sorted_ascii = list(ascii_matrix)
    #for i in range(sorted_ascii):
    #    for j in range(sorted_ascii)""
    sorted_ascii = np.array(sorted_ascii)
    sorted_ascii = np.sort(sorted_ascii)
    #print(ascii_matrix)
    #print(sorted_ascii)
    for f in sorted_ascii:
        key_matrix.append(ascii_matrix.index(f))
    return np.array(key_matrix)

# ---------------------------------------------------------------------------------------------------
def row_decrypt_single_stage(ciphertext: str, key: np.ndarray) -> str: 
    '''
    * This function simply applies one round of decryption to the input ciphertext.
    * Returns the decrypted string.
    '''
    plaintext = ""
    lister = []
    key_length = len(key)
    #print(key)
    #print(len(ciphertext))
    
    rows = len(ciphertext)// key_length
    matrix = [['']*key_length for _ in range(rows)]
    #print(matrix)

    ciph = []
    for c in ciphertext:
        ciph.append(ord(c)-97)
            
    char_index = 0
    
    for k_index,k_value in enumerate(key):
        for i in range(rows):
            #print(k_value)
            matrix[i][k_value] = ciph[char_index]
        char_index+=1
    for i in range(rows):
        lister.extend(matrix[i])
 
    
    for l in lister:
        plaintext+= chr(l+97)
    return plaintext

# ---------------------------------------------------------------------------------------------------
def row_decrypt(ciphertext: str, key: str, stage: int) -> str: 
    '''
    * Uses a row transposition cipher algorithm to decrypt the ciphertext message, using the provided key, and the number of stages in stage.
    * You may assume that Stage will be either 1 or 2.
    * If stage is greater than 1, the same key should be used to complete the higher-stage transposition process.
    * Remove any added padding values.
    * Returns the decrypted plaintext as a string of characters.
    '''
    

    key_mat = row_gen_key(key)
    key_length = len(key_mat)

    decrypted =""
    decrypted= row_decrypt_single_stage(ciphertext, key_mat)

    
    if stage == 2:
        temp = ""
        temp= row_decrypt_single_stage(decrypted, key_mat)
        decrypted = temp
    answer = ''
    for l in decrypted:
        if l != 'x':
            answer+= l
    return  answer

# ===============================================================================

#testPf()
#testhill()
#testRow()