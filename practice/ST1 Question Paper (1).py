# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np





### Q2  ############

K2 = '67ED1'
P22 = '57825EBF6D'
C23 = '1DB47C299C'


rand_perm1 = [32,30,35,6,21,29,18,38,24,27,39,16,10,2,37,26,4,9,5,40,14,8,25,3,13,28,19,12,34,33,20,22,7,15,31,1,23,11,17,36]#during permutation, bit 1 goest to position 32, bit 2 to position 30 etc.
rand_perm_key1 = [3,17,7,6,20,8,12,15,18,11,16,4,2,10,13,5,19,1,14,9] #during permutation, bit 1 goest to position 3, bit 2 to position 17 etc.
rand_perm_key2 = [14,15,8,18,4,5,7,6,11,2,17,13,10,1,12,3,16,9,19,20] #during permutation, bit 1 goest to position 14, bit 2 to position 15 etc.

def permutate(a,perm,length):
    a_b = bin(int(a,16))[2:].zfill(length)
    
    b = list(a_b)
    results = np.empty(length,dtype = str)

    for i in range(length):
     
        results[perm[i]-1] = b[i]
    
    x = hex(int(''.join(results),2))[2:].upper()
    return x

def rev_permutate(a,perm,length):
    a_b = bin(int(a,16))[2:].zfill(length)
    
    b = list(a_b)
    results = np.empty(length,dtype = str)

    for i in range(length):

        results[i] = b[perm[i]-1]
    

    x = hex(int(''.join(results),2))[2:].upper()

    return x

def shift(a,shift,length):
    a_b = bin(int(a,16))[2:].zfill(length)
    b = list(a_b)
    
    results = np.roll(b,shift)
    #print(results)
    x = hex(int(''.join(results),2))[2:].upper()
    return x

def xor(a,b):
    #l = int(a,16)
    #s = int(b,16)
    return hex(int(a,16)^int(b,16))[2:].upper()


def generate_des_key(key,perm1,perm2):
    permed1 = permutate(key,rand_perm_key1,20)
    keys = []
    
    for i in range(4):
        
        shifted = shift(permed1,(i+1)*(-2),20)
        permed2 = permutate(shifted, rand_perm_key2, 20)
        keys.append(permed2)
    
    return keys

des_keys = generate_des_key(K2, rand_perm_key1, rand_perm_key2)


def des_encrypt(message,keys):
    init_perm = permutate(message, rand_perm1, 40)
    l = []
    r = []
    meow = format(int(init_perm,16),'b')
    meow.zfill(40)
    #left = hex((int(meow,2)>>10) & 0b1111111111)[2:]
    #right = hex(int(meow,2) & 0b1111111111)[2:]
    left = init_perm[:5]
    right = init_perm[5:]
    for i in range(4):
        fed = xor(right,keys[i])
        temp = right
        right = xor(left,fed)
        left = temp
        l.append(left.upper())
        r.append(right.upper())
        
    swapped = right+left
    cipher = rev_permutate(swapped, rand_perm1, 40)
    print("XXXXXXXXX LEFT XXXXXXXXXX")
    print(l)
    print("XXXXXXXXX Right XXXXXXXXXX")
    print(r)
    return cipher

x = des_encrypt(P22, des_keys)
print(x)

#des_keys_inv = des_keys[::-1]
#y = des_encrypt(x, des_keys_inv)
#print(y)
#print(des_keys)
#print(des_keys_inv)
#print(C23)
#y = des_encrypt(C23, des_keys_inv)
#print(y)


## Q1 #############

IV1 = '45A2481A42656668'
K1 = 'BA4928B18710AC51'

print(len(K1))
print(len("0b1111111111111111111111111111111111110000000000000000000000000000"))
P11 = 'AFE897AE7D5DCE4A15D264059D923322FC81'
C12 = '36C326053274FD64CCF864283F9AAF7199D9'
def q1_encrypt(IV,plaintext,key):
    o = []
    cipher =""
    o_1 = (xor(IV,key))
    o.append(hex(np.bitwise_not(int(o_1,16)))[2:].upper())
    
    for i in range(4):

        s = o[i][i*9:i*9+9]
        
        cipher+= xor(plaintext[i*9:i*9+9], s)
        inp = o[i][i*9:i*9+9] +cipher
        o_2 = (xor(inp,key))
        #print(f'two {o_2}')
        o_temp =hex(np.bitwise_not(int(o_2,16)))[2:].upper()
        #o_temp = not o_temp
        #print(f'tem {o_temp}')
        
        o.append(o_temp)
        
    print(o)
    return cipher


def q1_decrypt(IV,cipher,key):
    o = []
    plaintext =""
    o_1 = (xor(IV,key))
    o.append(hex(np.bitwise_not(int(o_1,16)))[2:].upper())
    #print("CIPHER")
    #print(plaintext)
    
    for i in range(4):

        s = o[i][i*9:i*9+9]
        #print("SSS")
        #print(s)
        #print('MEOW')
        #print(plaintext[i*9:i*9+9])
        #print(plaintext[i*9:i*9+9])
        #print(s)
        
        print(cipher[i*9:i*9+9])
        plaintext+= xor(cipher[i*9:i*9+9], s)
        print(f'Plain: {plaintext}')
        inp = o[i][i*9:i*9+9] +cipher[i*9:i*9+9]
        
        o_2 = (xor(inp,key))
        #print(f'two {o_2}')
        
        o_temp =hex(np.bitwise_not(int(o_2,16)))[2:].upper()
        #o_temp = not o_temp
        print(f'tem {o_temp}')
        
        o.append(o_temp)
        
    #print(o)
    return plaintext

#x = q1_encrypt(IV1,P11, K1)
#print(x)
#y = q1_decrypt(IV1,C12, K1)
### Q3 ##############################################

K3 = '71AB1D609'
RC3 = ['7','5','3','1']

#def hex_to_matrix(hex_val)


