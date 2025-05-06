# CORRECT MATCHES MEMO ANSWER 2 with modulo 256 ***
P3 = '819203119288A4D422987C04C9A2B421'

word1 = P3[:len(P3)//2]
word2 = P3[len(P3)//2:]
word1 = bin(int(word1,16))[2:].zfill(64)
word2 = bin(int(word2,16))[2:].zfill(64)

a = 0x6A
b= 0xBB
c = 0x3C
d = 0xA5

def process_round(a,b,c,d,word):
    
    c = b^c^d
    b = a^b
    a = a^int(word[:8],2)
    d = d^int(word[8:],2)
    return a,b,c,d

def process_block(a,b,c,d,full_word):
    blocks = []
    a_init = a
    b_init =b
    c_init =c
    d_init=d
    for i in range(0,len(full_word),16):
        blocks.append(full_word[i:i+16])
    counter =0
    for block in blocks:
        counter+=1
        #print(block)
        a,b,c,d = process_round(a,b,c,d,block)
        abcd = f'{a:02X}'+ f'{b:02X}' + f'{c:02X}' + f'{d:02X}'
        print(f'round {counter} : {abcd}')
    a_f ,b_f,c_f,d_f = (a+a_init)%256,(b+b_init)%256,(c+c_init)%256,(d+d_init)%256
    abcd_f  = f'{a_f:02X}'+ f'{b_f:02X}' + f'{c_f:02X}' + f'{d_f:02X}'
    print(f'H {abcd_f}')
    return a_f,b_f,c_f,d_f

a1,b1,c1,d1 = process_block(a,b,c,d,word1)
a2,b2,c2,d2 = process_block(a1,b1,c1,d1,word2)
