import numpy as np
import string
from PIL import Image
#import matplotlib.pyplot as plt

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
    plaintext = "eiaofrjiouajsiof1124ajksnd"
    key = "12345678"



    keyPermChoice1 = np.load("DES_Arrays\\DES_Key_Permutation_Choice_1.npy")
    keyPermChoice2 = np.load("DES_Arrays\\DES_Key_Permutation_Choice_2.npy")
    keyRoundShifts = np.load("DES_Arrays\\DES_Round_Shifts.npy")
    sBoxes = np.load("DES_Arrays\\DES_sBoxes.npy")
    FexpansionBox = np.load("DES_Arrays\\DES_Expansion_Box.npy")
    FpermutationChoice = np.load("DES_Arrays\\DES_F_Function_Permutation.npy")
    initPerm = np.load("DES_Arrays\\DES_Initial_Permutation.npy")
    invInitPerm = np.load("DES_Arrays\\DES_Inverse_Initial_Permutation.npy")

    ciphertext = des_Encrypt_String(plaintext,key)
    #print(ciphertext)
    decrypted = des_Decrypt_String(ciphertext,key)
    #print(decrypted)
    img = Image.open('moyse.jpg')
    img_np = np.array(img)
    image_dim = img_np.shape
    # Encrypt
    #key = "ToonMouse2025"
    encrypted_img_np = des_Encrypt_Image(img_np, key)
    #encrypted_img_np = encrypted_img_np.reshape(image_dim)
    print(encrypted_img_np)
    encrypted_img_np = aes_des_rc4_Convert_To_Image(encrypted_img_np,image_dim)
    Image.fromarray(encrypted_img_np).save('encrypted_jerry_DES.png')
    
    # Decrypt
    decrypted_img_np = des_Decrypt_Image(encrypted_img_np, key)
    print(decrypted_img_np)
    #decrypted_img_np = decrypted_img_np.reshape(image_dim)
    decrypted_img_np = aes_des_rc4_Convert_To_Image(decrypted_img_np,image_dim)
    Image.fromarray(decrypted_img_np).save('decrypted_jerry_DES.png')
    """
    print("keyPermChoice1 #####################")
    print(keyPermChoice1)
    print("keyPermChoice2 #####################")
    print(keyPermChoice2)
    print("keyRoundShifts #####################")
    print(keyRoundShifts)
    print("#############################################")

    print("sBoxes #############################")
    print(sBoxes)
    print("FexpansionBox ######################")
    print(FexpansionBox)
    print("FpermutationChoice #################")
    print(FpermutationChoice)
    print("initPerm ###########################")
    print(initPerm)
    print("invInitPerm ########################")
    print(invInitPerm)
    """
    #x = des_Generate_Round_Keys(key,keyPermChoice1,keyPermChoice2,keyRoundShifts)
    #print(x)
    
    #print(des_Process_Round("FF00785500FF8066","502CAC572AC2",sBoxes,FexpansionBox,FpermutationChoice ))

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
    #encrypted_img_np = encrypted_img_np.reshape(image_dim)
    encrypted_img_np2 = aes_des_rc4_Convert_To_Image(encrypted_img_np,image_dim)
    #decrypted_img_np = aes_des_rc4_Convert_To_Image(decrypted_img_np,image_dim)
    Image.fromarray(encrypted_img_np2).save('encrypted_jerry.png')

    # Decrypt
    decrypted_img_np = rc4_Decrypt_Image(encrypted_img_np, key)
    #decrypted_img_np = decrypted_img_np.reshape(image_dim)
    decrypted_img_np = aes_des_rc4_Convert_To_Image(decrypted_img_np,image_dim)
    Image.fromarray(decrypted_img_np).save('decrypted_jerry.png')

def print_2d_array_hex(array):
    for row in array:
        for val in row:
            print(f"{val:0X}", end=" ")  # 4-digit hex, uppercase
        print()


def test_AES():
    sBox = np.load("AES_Arrays\\AES_Sbox_lookup.npy")
    invsBox = np.load("AES_Arrays\\AES_Inverse_Sbox_lookup.npy")
    #print("SBOX #############################################")
    #print(sBox)
    #print("INVSBOX ##########################################")
    #print(invsBox)
    mix_column_state = [ [0x52,0xDC,0xA2,0xE3],
                        [0xDB,0xCE,0xA2,0x43],
                        [0xB4,0xAD,0xC4,0xC1],
                        [0xE3,0xD5,0xA3,0xC5]
                        ]

    #s =aes_Mix_Columns_Encrypt(np.array(mix_column_state))
    #print_2d_array_hex(s)
    #e = aes_Mix_Columns_Decrypt(s)
    #print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    #print_2d_array_hex(e)

    #f = aes_Substitute_Bytes(e,sBox)
    #print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    #print_2d_array_hex(f)
    #print(f)
    #print("@@@@@@@@@@@@@@")
    #shifted = aes_Shift_Rows_Encrypt(f)
    #print(shifted)
    #print("@@@@@@@@@@@@@@@@@@")
    #print(aes_Shift_Rows_Decrypt(shifted))
    key = 'abcdefghijklmnopqrstuvwxyz123456'
    plaintext = "pikachuplsdie"
    x = aes_Generate_Round_Keys(key,sBox)
    #print(x)
    #cipher =  aes_Encrypt_String(plaintext,key)
    #print(cipher)
    #plain = aes_Decrypt_String(cipher,key)
    #print(plain)
       # Load image
    img = Image.open('moyse.jpg')
    img_np = np.array(img)
    image_dim = img_np.shape
    # Encrypt
    #key = "ToonMouse2025"
    encrypted_img_np = aes_Encrypt_Image(img_np, key)
    #encrypted_img_np = encrypted_img_np.reshape(image_dim)
    encrypted_img_np2 = aes_des_rc4_Convert_To_Image(encrypted_img_np,image_dim)
    #decrypted_img_np = aes_des_rc4_Convert_To_Image(decrypted_img_np,image_dim)
    Image.fromarray(encrypted_img_np2).save('encrypted_jerry_AES.png')

    # Decrypt
    decrypted_img_np = aes_Decrypt_Image(encrypted_img_np, key)
    #decrypted_img_np = decrypted_img_np.reshape(image_dim)
    decrypted_img_np = aes_des_rc4_Convert_To_Image(decrypted_img_np,image_dim)
    Image.fromarray(decrypted_img_np).save('decrypted_jerry_AES.png')
# ----------------------------------------------------------------------------------------------
# 3.1 AES Cipher
# ----------------------------------------------------------------------------------------------


def aes_Generate_Round_Keys(key: str, sBox: np.ndarray) -> np.ndarray: # 1
    key = [ord(k) for k in key]
    key_array = []
    for i in range(0, len(key), 4):
        block = key[i:i+4]
        key_array.append(block)
    #print(key_array)
    round_constants = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40]
    
    w = key_array.copy()
    rcon_iter = 0

    while len(w) < 60:
        temp = w[-1].copy()
        
        #  multiples of 8 gets affectes
        if len(w) % 8 == 0:
            # Rotate
            temp = temp[1:] + [temp[0]]
            
            # Sub bytes
            for i in range(4):
                row = (temp[i] >> 4) & 0x0F
                col = temp[i] & 0x0F
                result_byte = sBox[row][col]
                result_byte = result_byte[2:]  
                temp[i] = int(result_byte, 16)
            
            # xor round con
            temp[0] ^= round_constants[rcon_iter]
            rcon_iter += 1
        
        # sub every 4 words after 8th byte
        elif len(w) % 8 == 4:
            # Sub bytes
            for i in range(4):
                row = (temp[i] >> 4) & 0x0F
                col = temp[i] & 0x0F
                result_byte = sBox[row][col]
                # Convert from hex string to integer
                result_byte = result_byte[2:]  
                temp[i] = int(result_byte, 16)
        
        # xor with word *-8
        for i in range(4):
            temp[i] ^= w[-8][i]
        
        w.append(temp)
    
    round_keys = []
    for i in range(0, len(w), 4):
        round_key = np.array([w[i], w[i+1], w[i+2], w[i+3]]).T
        round_keys.append(round_key)
    
    return np.array(round_keys)



def aes_Preprocess_String_Plaintext(plaintext: str) -> np.ndarray: # 2

    ascii_values = [ord(char) for char in plaintext]
    
    block_size = 16
    padding_length = block_size - (len(ascii_values) % block_size)
    if padding_length == 0:
        padding_length = block_size
    
    padded_data = ascii_values + [padding_length] * padding_length

    return np.array(padded_data, dtype=int)


def aes_Create_Input_States(inputBytes: np.ndarray) -> np.ndarray: # 3
    total_states = []
    states = []
    for i in range(0,len(inputBytes),4):
        states.append(inputBytes[i:i+4])
    
    for i in range(0,len(states),4):
        temp = []
        temp.append(states[i])
        temp.append(states[i+1])
        temp.append(states[i+2])
        temp.append(states[i+3])
        total_states.append(temp)
    return np.array(total_states)


def aes_remove_Padding(paddedArray: np.ndarray) -> np.ndarray: # 4
    padding_length = paddedArray[-1]
    
    for i in range(1, padding_length + 1):
        if i <= len(paddedArray) and paddedArray[-i] != padding_length:
            return paddedArray
    
    return paddedArray[:-padding_length]


def aes_Encrypt_String(plaintext: str, key: str) -> np.ndarray: # 5
    sBox = np.load("AES_Arrays\\AES_Sbox_lookup.npy")

    processed = aes_Preprocess_String_Plaintext(plaintext)

    #print(f'processed: {processed}')
    roundKeys = aes_Generate_Round_Keys(key,sBox)
    #print(f'roundkeys: {roundKeys}')
    input_states =  aes_Create_Input_States(processed)
    #print(f'input: {input_states}')
    encrypted_states =[]
    for state in input_states:
        encrypted = aes_Encrypt_State(state,roundKeys,sBox)
        encrypted_states.append(encrypted)
    
    #print(f'encrypted: {encrypted_states}')
    encrypted_data = np.array([], dtype=int)
    for state in encrypted_states:
        flattened_state = state.flatten()
        encrypted_data = np.append(encrypted_data, flattened_state)
    
    return encrypted_data



def aes_Decrypt_String(ciphertext: np.ndarray, key: str) -> str: # 6
    sBox = np.load("AES_Arrays\\AES_Sbox_lookup.npy")
    invsBox = np.load("AES_Arrays\\AES_Inverse_Sbox_lookup.npy")

    roundKeys = aes_Generate_Round_Keys(key,sBox)
    input_states = aes_Create_Input_States(ciphertext)
    
    decrypted_states = []
    for state in input_states:
        decrypted = aes_Decrypt_State(state,roundKeys,invsBox)
        decrypted_states.append(decrypted)
    
    decrypted_data = np.array([], dtype=int)
    for state in decrypted_states:
        flattened_state = state.flatten()
        decrypted_data = np.append(decrypted_data, flattened_state)
    #print(decrypted_data)
    decrypted_data = aes_remove_Padding(decrypted_data)
    #print(decrypted_data)
    decrypted_text = ''.join(chr(int(b)) for b in decrypted_data)
    
    return decrypted_text


def aes_Preprocess_Image_Plaintext(plaintext: np.ndarray) -> np.ndarray: # 7
    flat_data = plaintext.flatten()
    
    # Apply padding (like string version but to 16 bytes)
    block_size = 16
    padding_length = block_size - (len(flat_data) % block_size)
    if padding_length == 0:
        padding_length = block_size

    padded_data = np.append(flat_data, [padding_length] * padding_length)

    return padded_data.astype(int)

def aes_Encrypt_Image(plaintext: np.ndarray, key: str) -> np.ndarray: # 8
    sBox = np.load("AES_Arrays\\AES_Sbox_lookup.npy")
    processed = aes_Preprocess_Image_Plaintext(plaintext)
    roundKeys = aes_Generate_Round_Keys(key, sBox)
    input_states = aes_Create_Input_States(processed)

    encrypted_states = []
    for state in input_states:
        encrypted = aes_Encrypt_State(state, roundKeys, sBox)
        encrypted_states.append(encrypted)
    
    encrypted_data = np.array([], dtype=int)
    for state in encrypted_states:
        flattened_state = state.flatten()
        encrypted_data = np.append(encrypted_data, flattened_state)
    encrypted_data = encrypted_data.astype(np.uint8)
    return encrypted_data


def aes_Decrypt_Image(ciphertext: np.ndarray, key: str) -> np.ndarray: # 9
    sBox = np.load("AES_Arrays\\AES_Sbox_lookup.npy")
    invsBox = np.load("AES_Arrays\\AES_Inverse_Sbox_lookup.npy")

    roundKeys = aes_Generate_Round_Keys(key, sBox)
    input_states = aes_Create_Input_States(ciphertext)

    decrypted_states = []
    for state in input_states:
        decrypted = aes_Decrypt_State(state, roundKeys, invsBox)
        decrypted_states.append(decrypted)
    
    decrypted_data = np.array([], dtype=int)
    for state in decrypted_states:
        flattened_state = state.flatten()
        decrypted_data = np.append(decrypted_data, flattened_state)

    # Remove padding
    decrypted_data = aes_remove_Padding(decrypted_data)
    decrypted_data = decrypted_data.astype(np.uint8)
    return decrypted_data


def aes_Add_Round_key(state: np.ndarray, roundKey: np.ndarray) -> np.ndarray: # 10
    return np.bitwise_xor(state, roundKey)




def aes_Substitute_Bytes(state: np.ndarray, sBox: np.ndarray) -> np.ndarray: # 11
    result = state.copy()
    for i in range(4):
        for j in range(4):
            byte = state[i][j]
            row = (byte >> 4) & 0x0F
            col = byte & 0x0F
            result_byte = sBox[row][col]
            result_byte = result_byte[2:]
            result_int = int(result_byte, 16)
            result[i][j] = result_int
    return result


def aes_Shift_Rows_Encrypt(state: np.ndarray) -> np.ndarray: # 12
    state[1] = np.roll(state[1],-1)
    state[2] = np.roll(state[2],-2)
    state[3] = np.roll(state[3],-3)
    return state


def aes_Shift_Rows_Decrypt(state: np.ndarray) -> np.ndarray: # 13
    state[1] = np.roll(state[1],1)
    state[2] = np.roll(state[2],2)
    state[3] = np.roll(state[3],3)    
        
    return state


def aes_Mix_Columns_Encrypt(state: np.ndarray) -> np.ndarray: # 14
    
    def gf_mul(a, b):
        p = 0
        for _ in range(8):
            if b & 1:
                p ^= a
            high_bit = a & 0x80  # 0x80 = 0b10000000
            a = (a << 1) & 0xFF
            if high_bit:
                a ^= 0x1B  # 0x1B = 0b00011011 
            b >>= 1
        return p
    result = state.copy()
    

    for col in range(4):
        s0 = state[0][col]
        s1 = state[1][col]
        s2 = state[2][col]
        s3 = state[3][col]
        
        result[0][col] = gf_mul(2, s0) ^ gf_mul(3, s1) ^ s2 ^ s3
        result[1][col] = s0 ^ gf_mul(2, s1) ^ gf_mul(3, s2) ^ s3
        result[2][col] = s0 ^ s1 ^ gf_mul(2, s2) ^ gf_mul(3, s3)
        result[3][col] = gf_mul(3, s0) ^ s1 ^ s2 ^ gf_mul(2, s3)
    
    return result

def aes_Mix_Columns_Decrypt(state: np.ndarray) -> np.ndarray: # 15
    def gf_mul(a, b):
        p = 0
        for _ in range(8):
            if b & 1:
                p ^= a
            high_bit = a & 0x80  # 0x80 = 0b10000000
            a = (a << 1) & 0xFF
            if high_bit:
                a ^= 0x1B  # 0x1B = 0b00011011 
            b >>= 1
        return p
        
    result = state.copy()
   
    for col in range(4):
        s0 = state[0][col]
        s1 = state[1][col]
        s2 = state[2][col]
        s3 = state[3][col]
       
        result[0][col] = gf_mul(0x0E, s0) ^ gf_mul(0x0B, s1) ^ gf_mul(0x0D, s2) ^ gf_mul(0x09, s3)
        result[1][col] = gf_mul(0x09, s0) ^ gf_mul(0x0E, s1) ^ gf_mul(0x0B, s2) ^ gf_mul(0x0D, s3)
        result[2][col] = gf_mul(0x0D, s0) ^ gf_mul(0x09, s1) ^ gf_mul(0x0E, s2) ^ gf_mul(0x0B, s3)
        result[3][col] = gf_mul(0x0B, s0) ^ gf_mul(0x0D, s1) ^ gf_mul(0x09, s2) ^ gf_mul(0x0E, s3)
   
    return result

def aes_Apply_Encryption_Round(state: np.ndarray, roundKey: np.ndarray, sBox: np.ndarray) -> np.ndarray: # 16
    state = aes_Substitute_Bytes(state, sBox)
    state = aes_Shift_Rows_Encrypt(state)
    state = aes_Mix_Columns_Encrypt(state)
    state = aes_Add_Round_key(state, roundKey)
    
    return state


def aes_Encrypt_State(state: np.ndarray, roundKeys: np.ndarray, sBox: np.ndarray) -> np.ndarray: # 17
    state = aes_Add_Round_key(state, roundKeys[0])
    # rounds 1-13 

    for round_num in range(1, 14):
        state = aes_Apply_Encryption_Round(state, roundKeys[round_num], sBox)
    # Final round 
    state = aes_Substitute_Bytes(state, sBox)   
    state = aes_Shift_Rows_Encrypt(state)
    state = aes_Add_Round_key(state, roundKeys[14])
    return state

def aes_Apply_Decryption_Round(state: np.ndarray, roundKey: np.ndarray, sBox: np.ndarray) -> np.ndarray: # 18

    state = aes_Add_Round_key(state, roundKey)
    state = aes_Mix_Columns_Decrypt(state)
    state = aes_Shift_Rows_Decrypt(state)
    state = aes_Substitute_Bytes(state, sBox)
    
    return state


def aes_Decrypt_State(state: np.ndarray, roundKeys: np.ndarray, sBox: np.ndarray) -> np.ndarray: # 19
    # Initial round
    state = aes_Add_Round_key(state, roundKeys[14])
    
    # Main rounds
    for round_num in range(13, 0, -1):
        state = aes_Shift_Rows_Decrypt(state)
        state = aes_Substitute_Bytes(state, sBox)
        state = aes_Add_Round_key(state, roundKeys[round_num])
        state = aes_Mix_Columns_Decrypt(state)
    
    # Final round
    state = aes_Shift_Rows_Decrypt(state)
    state = aes_Substitute_Bytes(state, sBox)
    state = aes_Add_Round_key(state, roundKeys[0])
    
    return state


def aes_des_rc4_Convert_To_Image(arrayToConvert: np.ndarray, originalShape: tuple) -> np.ndarray: # 20
    result = np.zeros(originalShape, dtype=np.uint8)
    expected_size = originalShape[0] * originalShape[1] * originalShape[2]
    PAD_VALUE = 255
    # If the array is smaller than the original image, we need padding
    if len(arrayToConvert) < expected_size:
        padded_array = np.full(expected_size, PAD_VALUE, dtype=np.uint8)
        padded_array[:len(arrayToConvert)] = arrayToConvert
        result = padded_array.reshape(originalShape)
    
    # If the array is larger than the original image, we need to truncate
    elif len(arrayToConvert) > expected_size:
        result = arrayToConvert[:expected_size].reshape(originalShape)
    
    # If the array is exactly the right size, just reshape
    else:
        result = arrayToConvert.reshape(originalShape)
    
    return result



# ----------------------------------------------------------------------------------------------
# 3.2 DES Cipher
# ----------------------------------------------------------------------------------------------
    
def des_Generate_Round_Keys(key: str, permutedChoice1, permutedChoice2, roundShifts) -> np.ndarray: # 1
    key_str = key.encode('ascii').hex()
    permed1 = des_Apply_Permutation(key_str, permutedChoice1, 64)
    
    keys = []
    total_shifts = 0
    
    for shifts in roundShifts:
        total_shifts += shifts
        shifted = des_left_Shift(permed1, total_shifts)
        round_key = des_Apply_Permutation(shifted, permutedChoice2, 56)
        keys.append(round_key)

    return np.array(keys)
    

def des_Preprocess_String_Plaintext(plaintext: str) -> np.ndarray: # 2
    plain_hex = []

    for char in plaintext:
        plain_hex.append(char.encode('ascii').hex())
   
    if len(plain_hex)%8 != 0:
        pad_len = 8-(len(plain_hex)%8)
        for i in range(pad_len):
            plain_hex.append(f'{pad_len:02X}')
            
    
    elif  len(plain_hex)%8 == 0: 
        for i in range(8):
            plain_hex.append('08')
    #print(f"PROCESSED FOOD YUM {plain_hex}")
    return np.array(plain_hex)


def des_Create_Input_Blocks(processedArray: np.ndarray) -> np.ndarray: # 3
    blocks = []
    #print(f'LENGTH DURING BLOCK CREATION : {len(processedArray)}')
    for i in range(0,len(processedArray),8):
        block = processedArray[i:i+8]
        block_str = ''.join(block)
        blocks.append(block_str)
    return np.array(blocks)


def des_Remove_String_Padding(paddedArray: np.ndarray) -> np.ndarray: # 4
    
    padding = paddedArray[-1]
    pad_len = int(padding,16)

    return paddedArray[:-pad_len] 


def des_Encrypt_String(plaintext: str, key: str) -> np.ndarray: # 5
    keyPermChoice1 = np.load("DES_Arrays\\DES_Key_Permutation_Choice_1.npy")
    keyPermChoice2 = np.load("DES_Arrays\\DES_Key_Permutation_Choice_2.npy")
    keyRoundShifts = np.load("DES_Arrays\\DES_Round_Shifts.npy")
    sBoxes = np.load("DES_Arrays\\DES_sBoxes.npy")
    FexpansionBox = np.load("DES_Arrays\\DES_Expansion_Box.npy")
    FpermutationChoice = np.load("DES_Arrays\\DES_F_Function_Permutation.npy")
    initPerm = np.load("DES_Arrays\\DES_Initial_Permutation.npy")
    invInitPerm = np.load("DES_Arrays\\DES_Inverse_Initial_Permutation.npy")

    text = des_Preprocess_String_Plaintext(plaintext)
    #print(f'original plaintext: {text}')
    keys = des_Generate_Round_Keys(key,keyPermChoice1,keyPermChoice2,keyRoundShifts)
    blocks = des_Create_Input_Blocks(text)

    ciphertext = []
    for b in blocks:
        #print(f"ENCRYPT B: {b}")
        cipher = des_Process_Block(b,keys,initPerm,sBoxes,FexpansionBox,FpermutationChoice,invInitPerm)
        #print(f"CIPHER BLOCK ENCRYPTION: {cipher}")
        for i in range(0,len(cipher),2):
            c = cipher[i:i+2]
            ciphertext.append(c)

    return np.array(ciphertext)


def des_Decrypt_String(ciphertext: np.ndarray, key: str) -> str: # 6
    # Load required tables
    keyPermChoice1 = np.load("DES_Arrays\\DES_Key_Permutation_Choice_1.npy")
    keyPermChoice2 = np.load("DES_Arrays\\DES_Key_Permutation_Choice_2.npy")
    keyRoundShifts = np.load("DES_Arrays\\DES_Round_Shifts.npy")
    sBoxes = np.load("DES_Arrays\\DES_sBoxes.npy")
    FexpansionBox = np.load("DES_Arrays\\DES_Expansion_Box.npy")
    FpermutationChoice = np.load("DES_Arrays\\DES_F_Function_Permutation.npy")
    initPerm = np.load("DES_Arrays\\DES_Initial_Permutation.npy")
    invInitPerm = np.load("DES_Arrays\\DES_Inverse_Initial_Permutation.npy")
    

    cipher_blocks = []
    cipher_blocks = des_Create_Input_Blocks(ciphertext)
    #print(f'cipherblocks: {cipher_blocks}')

    keys = des_Generate_Round_Keys(key, keyPermChoice1, keyPermChoice2, keyRoundShifts)
    inv_keys = keys[::-1]  # Reverse the keys for decryption
    
    plaintext = []
    for b in cipher_blocks:
        #print(f'CIPHER BLOCK TO BE PROCESSED: {b}')
        plain = des_Process_Block(b, inv_keys, initPerm, sBoxes, FexpansionBox, FpermutationChoice, invInitPerm)
        #print(f'PROCESSED CIPHERBLOCK: {plain}')
        for i in range(0, len(plain), 2):
            p = plain[i:i+2]
            plaintext.append(p)
    
    # Remove padding
    #decrypted = des_Remove_String_Padding(np.array(plaintext))
    decrypted = plaintext
    #print(f'decrypted_plaintext: {decrypted}')
 
    final_decrypted = ""
    for d in decrypted:
        try:
            dec_char = bytes.fromhex(d).decode('ascii')
            final_decrypted += dec_char
        except:

            dec_char = chr(int(d, 16))
            final_decrypted += dec_char
    
    return final_decrypted


def des_Process_Block(block: str, roundKeys: np.ndarray, initialPerm: np.ndarray, sBoxes: np.ndarray,
                      expansionBox: np.ndarray, FpermChoice: np.ndarray, invInitialPerm: np.ndarray) -> str: # 7
    initial = des_Apply_Permutation(block,initialPerm,64)

    for key in roundKeys:
        initial  = des_Process_Round(initial,key,sBoxes,expansionBox,FpermChoice)
    
    split = des_Split_In_Two(initial)
    left = split[0]
    right = split[1]
    new_str = right+left
    inv_perm = des_Apply_Permutation(new_str,invInitialPerm,64)

    return inv_perm



def des_Process_Round(roundInputValue: str, roundKey: str, sBoxes: np.ndarray, expansionBox: np.ndarray, 
                      permutationChoice: np.ndarray) -> str: # 8
    
    split = des_Split_In_Two(roundInputValue)
    left = split[0]
    right = split[1]
    
    expanded = ""
    right_bin = bin(int(right,16))[2:].zfill(32)
    
    for i in expansionBox:
        expanded+= right_bin[i-1]
    
    expanded = f'{int(expanded,2):0X}'
    xored_right = des_XOR(expanded,roundKey)

    bin_xored_right = bin(int(xored_right,16))[2:]
    bin_xored_right = bin_xored_right.zfill(48)
    sbox_permuted = ""
    box_int = 0    
    for i in range(0,48,6):

        block = bin_xored_right[i:i+6]
        row_bits = block[0] + block[5] 
        col_bits = block[1]+block[2]+block[3]+block[4]
        row = int(row_bits,2)
        col = int(col_bits,2)
        
        sbox_bin = bin(sBoxes[box_int][row][col])[2:].zfill(4)

        box_int+=1
        sbox_permuted+= sbox_bin


    sbox_hex = f'{int(sbox_permuted,2):0X}' 
    fpermed = des_Apply_Permutation(sbox_hex,permutationChoice,32)
    new_right = des_XOR(left,fpermed)
    new_left = right

    return new_left+new_right
    


def des_Preprocess_Image_Plaintext(plaintext: np.ndarray) -> np.ndarray: # 9
    flattened = plaintext.flatten()
    

    hex_values = [f'{value:02X}' for value in flattened]
    
    
    block_size = 8
    padding_length = block_size - (len(hex_values) % block_size)
    if padding_length == 0:
        padding_length = block_size
    
    # Apply PKCS5 padding (each padding byte = number of padding bytes)
    padded_data = hex_values + [f'{padding_length:02X}'] * padding_length
    
    return np.array(padded_data)


def des_Remove_Image_Padding(paddedArray: np.ndarray) -> np.ndarray: # 10

    last_byte = paddedArray[-1]
    pad_len = int(last_byte, 16)
    
    for i in range(1, pad_len + 1):
        if paddedArray[-i] != f'{pad_len:02X}':
            #raise ValueError("Invalid padding detected")
            return paddedArray
    # Remove padding
    return paddedArray[:-pad_len]


def des_Encrypt_Image(plaintext: np.ndarray, key: str) -> np.ndarray: # 11
    keyPermChoice1 = np.load("DES_Arrays\\DES_Key_Permutation_Choice_1.npy")
    keyPermChoice2 = np.load("DES_Arrays\\DES_Key_Permutation_Choice_2.npy")
    keyRoundShifts = np.load("DES_Arrays\\DES_Round_Shifts.npy")
    sBoxes = np.load("DES_Arrays\\DES_sBoxes.npy")
    FexpansionBox = np.load("DES_Arrays\\DES_Expansion_Box.npy")
    FpermutationChoice = np.load("DES_Arrays\\DES_F_Function_Permutation.npy")
    initPerm = np.load("DES_Arrays\\DES_Initial_Permutation.npy")
    invInitPerm = np.load("DES_Arrays\\DES_Inverse_Initial_Permutation.npy")
    processed_data = des_Preprocess_Image_Plaintext(plaintext)
    
    # Generate round keys
    keys = des_Generate_Round_Keys(key, keyPermChoice1, keyPermChoice2, keyRoundShifts)
    
    # Create input blocks
    blocks = des_Create_Input_Blocks(processed_data)
    
    # Encrypt each block
    ciphertext = []
    for b in blocks:
        cipher = des_Process_Block(b, keys, initPerm, sBoxes, FexpansionBox, FpermutationChoice, invInitPerm)
        for i in range(0, len(cipher), 2):
            c = cipher[i:i+2]
            int_value = int(c, 16)
            ciphertext.append(int_value)
    
    return np.array(ciphertext)


def des_Decrypt_Image(ciphertext: np.ndarray, key: str) -> np.ndarray: # 12
    keyPermChoice1 = np.load("DES_Arrays\\DES_Key_Permutation_Choice_1.npy")
    keyPermChoice2 = np.load("DES_Arrays\\DES_Key_Permutation_Choice_2.npy")
    keyRoundShifts = np.load("DES_Arrays\\DES_Round_Shifts.npy")
    sBoxes = np.load("DES_Arrays\\DES_sBoxes.npy")
    FexpansionBox = np.load("DES_Arrays\\DES_Expansion_Box.npy")
    FpermutationChoice = np.load("DES_Arrays\\DES_F_Function_Permutation.npy")
    initPerm = np.load("DES_Arrays\\DES_Initial_Permutation.npy")
    invInitPerm = np.load("DES_Arrays\\DES_Inverse_Initial_Permutation.npy")
    print("ciphertext in des fn")
    print(ciphertext)
    ciphertext_flat = ciphertext.flatten()
    print("ciphertext in des flattened")
    print(ciphertext_flat)
    ciphertext_hex = np.array([f'{x:02x}'for x in ciphertext_flat])
    print("ciphertext hex")
    print(ciphertext_hex)
    cipher_blocks = des_Create_Input_Blocks(ciphertext_hex)
    
    # Generate and reverse the round keys for decryption
    keys = des_Generate_Round_Keys(key, keyPermChoice1, keyPermChoice2, keyRoundShifts)
    inv_keys = keys[::-1]  # Reverse the keys for decryption
    
    # Decrypt each block
    plaintext = []
    for b in cipher_blocks:
        print(f"block: {b}")
        plain = des_Process_Block(b, inv_keys, initPerm, sBoxes, FexpansionBox, FpermutationChoice, invInitPerm)
        for i in range(0, len(plain), 2):
            p = plain[i:i+2]
            plaintext.append(p)
    
    # Remove padding
    decrypted = des_Remove_Image_Padding(np.array(plaintext))
    
    # Convert hex strings back to integers
    decrypted_integers = np.array([int(hex_val, 16) for hex_val in decrypted], dtype=np.uint8)
    
    return decrypted_integers


def des_Apply_Permutation(valueToPermute: str, permuteTable: np.ndarray, numBitsBeforePermute: int) -> str: # 13
    
    bin_str = bin(int(valueToPermute, 16))[2:].zfill(numBitsBeforePermute)
    permuted = ''.join(bin_str[i - 1] for i in permuteTable.flatten()) 
    return f'{int(permuted,2):0X}'


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
    int_value = int(inputValue, 16)
    bin_value = bin(int_value)[2:].zfill(56)  # Assuming 56-bit input from PC-1
    

    left_half = bin_value[:28]
    right_half = bin_value[28:]
    
 
    left_shifted = left_half[shiftCount:] + left_half[:shiftCount]
    right_shifted = right_half[shiftCount:] + right_half[:shiftCount]
    
    
    combined = left_shifted + right_shifted
    
    result = int(combined, 2)
    return f'{result:X}'


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



# ----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------
test_AES()
#key = 'abcdefghijklmnopqrstuvwxyz123456'
#plaintext = "1111111111111111111"
#test_result = debug_aes_encryption_decryption(plaintext,key)
#test_DES()
#test_RC4()