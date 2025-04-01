# CORRECT

# NOTES:
# 1. He normally wants the L and R values AFTER each encryption round, and BEFORE each decryption round.
#       This way, you'll get the same L and R values (just in reverse), for encrypting something and then
#       decrypting it again.

import numpy as np


def permute(a,perm,length):
    # He normally defines perm as send element i to the position in perm[i]
    a_b = list(bin(int(a,16))[2:].zfill(length))

    result = np.empty(length,dtype=object)

    for i in range(len(a_b)):
        result[perm[i]-1] = a_b[i]

    return hex(int(''.join(result),2))[2:].zfill(length//4).upper()

def reverse_permute(a,perm,length):
    # He normally defines perm as send element i to the position in perm[i]
    a_b = list(bin(int(a,16))[2:].zfill(length))

    result = np.empty(length,dtype=object)

    for i in range(len(a_b)):
        result[i] = a_b[perm[i]-1]

    return hex(int(''.join(result),2))[2:].zfill(length//4).upper()


def xor(a,b,len):
    return hex(int(a,16) ^ int(b,16))[2:].zfill(len//4).upper()


def circ_shift(a,num):
    a_b = list(bin(int(a,16))[2:].zfill(16))
    rolled = np.roll(a_b,num)
    return hex(int(''.join(rolled),2))[2:].zfill(4).upper()


def generate_round_keys(key,perm1,perm2):
    # do init perm
    permed1 = permute(key,perm1,16)

    # generate the keys
    res = []
    for i in range(4):
        shifted = circ_shift(permed1,(i+1)*(-2))
        res.append(permute(shifted,perm2,16))

    return res


def encrypt(plaintext, keys, init_perm):
    # initial permutation
    permed = permute(plaintext,init_perm,32)

    l = []
    r = []

    left = permed[:4]
    right = permed[4:]
    for i in range(4):
        l.append(left)
        r.append(right)
        fed = xor(right,keys[i],16)
        xored = xor(left, fed, 16)
        left = right
        right = xored
        

    swapped = right + left

    # undo the permutation
    return reverse_permute(swapped,init_perm,32)


#initial permutation
init_perm1 = [13, 26, 32, 19, 25,  8, 10,  6, 27, 16, 21, 31,  2, 14,  9, 7, 12, 24,  1,  3, 20, 18,  5, 28, 30, 22, 23, 17, 29,  4, 11, 15]
#permuted choice 1
key_perm1 = [4,  3, 13, 12, 10,  7, 14,  6, 15,  2, 11,  9,  5,  1,  8, 16] 
#permuted choice 2
subkeyperm1 = [3, 13,  7,  9,  4,  2, 16, 15, 14, 11, 12, 10,  6,  1,  5,  8] 

k = '4A9F'
print(generate_round_keys(k,key_perm1,subkeyperm1))

# print(encrypt('A25395C4',['EE43', '7CF0', '0EBE', '651F'],init_perm1))
keys = ['EE43', '7CF0', '0EBE', '651F']
print(encrypt('FA3591E7',keys[::-1],init_perm1))