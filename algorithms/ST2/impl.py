
import numpy as np

#QUESTION 1 [30]
V11= 'FA2362D631A9CD93' #(V1)
K11 = 0xD934B5165BD5D4AE #(K1)
K21 = 0x8BF12EAAF81A83D5 #(K2)
DT1 = ['3AFCC8B41E9C2C3D','F2B32CEFE3BFE056','E59D4B5E588EEFB0','4F0672F054F3D5EF']



def encrypt(plain,key):
    left = plain[:8]
    right = plain[8:]
    swapped = right+left
    swapped_bin = bin(int(swapped,16))[2:].zfill(64)
    swapped_list = list(swapped_bin)
    shifted = np.roll(swapped_list,-8)
    shift= ''.join(shifted)
    int_shift = int(shift,2)
    return f'{key^int_shift:016X}'

def decrypt(cipher,key):
    xored = key^int(cipher,16)
    xored_bin = bin(xored)[2:].zfill(64)
    xored_list = list(xored_bin)
    shifted = np.roll(xored_list,8)
    shift= ''.join(shifted)
    plain = f'{int(shift,2):016X}'
    left = plain[:8]
    right = plain[8:]
    return right+left


X = []

for D in DT1:
    x = encrypt(D, K11)
    x = decrypt(D,K21)
    x = encrypt(D,K11)
    X.append(x)

seed = V11
R_a =[]
V_a = []
for y in X:
    new_x = f'{int(y,16)^int(seed,16):016X}'
    
    R = encrypt(new_x, K11)
    R = decrypt(R,K21)
    R = encrypt(R,K11)
    R_a.append(R)
    
    new_x = f'{int(y,16)^int(R,16):016X}'
    V = encrypt(new_x, K11)
    V = decrypt(V,K21)
    V= encrypt(V,K11)
    seed = V
    V_a.append(V)

#print(f'RA : {R_a}')
#print(f'VA : {V_a}')
P12 = 'B9F332CA4FF3766F3F96EAD3300139AB2E28E2B992DB285313F7CBDCCEBAA4C3'
C12 = [''] #[5]
#1.3
C13 = 'C8D801BB8F6F765DE26D5D0E3DFFB055D19F6378058E5AE4B60CB9E379124BE5'
P13 = [''] #[5]
seeds = []
ciphs =[]
#print(len(P12[0]))
for i in range(0,64,16):     
    seeds.append(P12[i:i+16])
    ciphs.append(C13[i:i+16])
#1.1
X11 = ['4518882CA71D60B0', '66D4E3E4E8F93B4D', '57DB05F3C69E8AF6', '2AE15A595DA724FA'] #[2.5] X1 to X4 (output of first EDE that takes DTi as input) 
R11 = ['3F5C0D15C3F07943', 'ED70D2AAC424B781', '3EB621AB5EFD514F', '120E996833D7191D'] #[15] R1 to R4  
V11 = ['66E8DDD0BC9FBAB1', '567DE2215C2BCDF9', 'E82A97C3953EDB4D', 'FBCCC99217D9B2BB'] #[2.5] V2 to V5    
#1.2
CLAP =''
PLAP = ''
for i in range(len(seeds)):
    xored = int(seeds[i],16)^int(R11[i],16)
    xored2 = int(ciphs[i],16)^int(R11[i],16)
    CLAP+= f'{xored:016X}'
    PLAP+= f'{xored2:016X}'
#print(f'CLAP {CLAP}')
#print(f'PLAP {PLAP}')

    
#print(R_a)
#print(V_a)

#print(X)
    

#QUESTION 2 [30]

C2_H2 = '406A5D4289A049379337A37E9C3D062E6B47FBF6' #(C2|H2) chipertext with appended hash code (hash calculated on plaintext)
			
P2 = '' #decrypted message [15] 				
H2 = ['','','','']  #[15] simple hash function output after each processed block (after circular right shift)

C2_H2 = '406A5D4289A049379337A37E9C3D062E6B47FBF6'
c_arr = []
for i in range(0,len(C2_H2),2):
    c_arr.append(int(C2_H2[i:i+2],16))

#print(c_arr)
plain = ''
d = 23
n= 187
for c in c_arr:
    plain+= f'{pow(c,d,n):02X}'
#print(plain)
#def rsa(plaintext):

p_blocks = []

for p in range(0,len(plain)-8,8):
    p_blocks.append(plain[p:p+8])    


#print(p_blocks)
def hash(blocks):
    hash_val = []
    hash_tot =0
    ct = 0
    for b in blocks:
        
        int_block = int(b,16)
        hash_tot = hash_tot^int_block
        bin_block = bin(hash_tot)[2:].zfill(32)
        bin_list = list(bin_block)
        shifted = np.roll(bin_list,1)
        shift = ''.join(shifted)
        hasher = int(shift,2)
        hash_tot = hasher
        hashs = f'{hasher:0X}'
        hash_val.append(hashs)
        
    return hash_val

print(hash(p_blocks))
      
P3 = '9652FE55E72D7D61A82C7D573A8662D1B0A3D9FEDD70BBEAF13A6C12C515F73C'
IV3 = '6A09BB673C6EA54F510E9B051F835BE0' #IV = a|b|c|d|e|f|g|h
K3 = [0x428A,0x7137,0xB5C0,0xE9B5]
    

def right_rotate(rot,n):
    bin_list = list(bin(int(rot,16))[2:].zfill(16))
    res = np.roll(bin_list,n)
    result = ''.join(res)
    return int(result,2)


def not_int(inte,length):
    inte = bin(inte)[2:].zfill(length)
    new_bin = ''
    for i in inte:
        if i == '0':
            new_bin+='1'
        else:
            new_bin+='0'
    return int(new_bin,2)
       
def encrypt_round(a,b,c,d,e,f,g,h,key,word):
    old_a = a
    old_e = e
    h=g
    g =f
    f = old_e
    d= c
    c=b
    b= old_a   

    CHefg =(int(e,16)& int(f,16))^(not_int(int(e,16), 4*4) ^int(g,16))
    
    maj_abc = (int(a,16)&int(b,16))^(int(a,16)&int(c,16))^(int(b,16)&int(c,16))
    sigma_a = f'{right_rotate(old_a, 4)^right_rotate(old_a, 8):04X}'   
    sigma_e = f'{right_rotate(old_e, 12)^right_rotate(old_e, 16):04X}'   
    supla= CHefg^int(h,16)^int(sigma_e,16)^word^key
    e = supla^int(d,16)
    a= int(sigma_a,16)^maj_abc^supla
    a = f'{a:04X}'
    e = f'{e:04X}'
    return a,b,c,d,e,f,g,h

block_3 = []
for i in range(0,len(IV3),4):
    block_3.append(IV3[i:i+4])

a = block_3[0]
b = block_3[1]
c = block_3[2]
d = block_3[3]
e = block_3[4]
f = block_3[5]
g = block_3[6]
h = block_3[7]

words = []
for i in range(0,64,16):     
    words.append(P3[i:i+16])

def process_block(word,a,b,c,d,e,f,g,h,key):
    a_i = int(a,16)
    b_i = int(b,16)
    c_i = int(c,16)
    d_i = int(d,16)
    e_i = int(e,16)
    f_i = int(f,16)
    g_i = int(g,16)
    h_i = int(h,16)
    abcdefgh = []
    split_words = []
    for i in range(0,16,4):
        split_words.append(int(word[i:i+4],16))
    
    for i in range(4):
        a,b,c,d,e,f,g,h = encrypt_round(a,b,c,d,e,f,g,h,K3[i],split_words[i])
    
    abcdefgh.append(a+b+c+d+e+f+g+h)
    print(f' ABCDEFGH :{abcdefgh}')
    a_f = int(a,16)
    b_f = int(b,16)
    c_f = int(c,16)
    d_f = int(d,16)
    e_f = int(e,16)
    f_f = int(f,16)
    g_f = int(g,16)
    h_f = int(h,16)
    a_ = f'{a_i^a_f:04X}'
    b_ = f'{b_i^b_f:04X}'
    c_ = f'{c_i^c_f:04X}'
    d_ = f'{d_i^d_f:04X}'
    e_ = f'{e_i^e_f:04X}'
    f_ = f'{f_i^f_f:04X}'
    g_ = f'{g_i^g_f:04X}'
    h_ = f'{h_i^h_f:04X}'
    hasher = a_+b_+c_+d_+e_+f_+g_+h_
    print(f'HASH {hasher}')
    return a_,b_,c_,d_,e_,f_,g_,h_

for i in range(4):
    print(i)
    a,b,c,d,e,f,g,h = process_block(words[i], a, b, c, d, e, f, g, h, K3)    
    """
    0
 ABCDEFGH :['E6190E2E49D51B893D52AC26F198D224']
HASH 8C10B54975BBBEC66C5C3723EE1B89C4
1
 ABCDEFGH :['26E04E205A4FC1088D64488811B8E943']
HASH C0F9400E139ADA81B036E4AEE0203B67
2
 ABCDEFGH :['0721D2871A15CB62E43EAAC9D12A5585']
HASH 21C19CA7405A0A6A695AE241C092BCC6
3
 ABCDEFGH :['BF372A648430A62815F791B2525B8A69']
HASH B816F8E39E256D4AF1C93B7B8371DFEC
    """