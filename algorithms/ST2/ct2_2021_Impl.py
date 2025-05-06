import numpy as np
#QUESTION 1

P11 = '902081C0'
K11 = 0x4E0EFD31
C11 = '4D8FDD70'

C12 = '9F11C60D'
K12 = 0xD740469C
P12 = ''		 #Plaintext (hex)

def encrypt(plaintext,key):
    left = plaintext[:4]
    right = plaintext[4:]
    swapped = right + left
    swapped_bin = bin(int(swapped,16))[2:].zfill(32)
    swapped_list = list(swapped_bin)

    shifted = np.roll(swapped_list,-1)
    shifted_bin = ''.join(shifted)

    return  f'{int(shifted_bin,2)^key:08X}'

def decrypt(cipher,key):
    cipher1 = f'{int(cipher,16)^key:08X}'
    cipher_bin = bin(int(cipher1,16))[2:].zfill(32)
    cipher_list = list(cipher_bin)
    shifted = np.roll(cipher_list,1)
    shifted_bin = ''.join(shifted)
    plain = f'{int(shifted_bin,2):08X}'
    left = plain[:4]
    right = plain[4:]
    swapped = right + left
    return  swapped

P12 = decrypt(C12,K12)
# print(P12) C048A428 CORRECT
"""
#QUESTION 1
P12_ans = 'C048A428' #[15]
"""


#QUESTION 2

P2_MAC = 'D8A503441106B0C6501491275E172002400000309366C50A'
K2 = 0xC4C84A40
H =   '' #calculated hash code (hex)
MAC = '' #calculated MAC (hex)
AUTH = '' #'YES' or 'NO'

def simple_hash(message_blocks):
    
    hash_value = 0
    
    for block in message_blocks:
        
        block_int = int(block, 16)
        hash_value ^= block_int
    return f"{hash_value:08X}"

blocks = []
for i in range(0,len(P2_MAC)-8,8):
    blocks.append(P2_MAC[i:i+8])


x  = simple_hash(blocks)
#print(x) # '87A00297'  MATCHES
#print(encrypt(x,K2)) # 'C1E74500' MATCHES

# encrypted x != last 8 digits of P2_MAC

"""
#QUESTION 2
H_ans = '87A00297'   #[12]
MAC_ans = 'C1E74500' #[3]
AUTH_ans = 'NO' 	 #[5]
"""

#QUESTION 3
K3_dec = [] #key (decimal/base 10)
K3_bin = '' #32-bit key (binary/base 2)
C3 = '385D1F04'
P3 = ''     #plaintext (hex)


q = 29
alpha = 11
Ya = 5
Yb = 12

def get_key(Ya, Yb, alpha, q):
    # get Xa
    Xa = -1
    for i in range(q):
        if pow(alpha,i) % q == Ya:
            Xa = i
            break
    
    # get the symmetric key
    return pow(Yb,Xa) % q

k = get_key(Ya,Yb, alpha, q)
#print(k)
k_bin = bin(k)[2:].zfill(8)
k_bin = k_bin*4
#print(k_bin)
k_hex =f'{int(k_bin,2):0X}'

plain = decrypt(C3,int(k_hex,16))
#print(plain)
"""
#QUESTION 3 MATCHES
K3_dec_ans = [28] 	  #[10]
K3_bin_ans = '00001110000111000001110000011100' #[2]
P3_ans = '818C1220'   #[3]
"""