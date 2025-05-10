# Alex Theodorou
P3 = '6B486E1E'
IV3 = '84BC'


H13 = '' #final SHA-16 MD [6]

message = bin(int(P3,16))[2:].zfill(32)
a = 0x8
b = 0x4
c= 0xB
d= 0xC

def process_round(a,b,c,d,word):
    c = b^c^d
    b = a^b
    a = a^ int(word[0:4],2)
    d = d^int(word[4:8],2)

    return a,b,c,d

def process_message(a,b,c,d,message):
    a3 = [] #output for round 1 to 4 [6]
    b3 = [] #output for round 1 to 4 [6]
    c3 = [] #output for round 1 to 4 [6]
    d3 = [] #output for round 1 to 4 [6]
    blocks = []
    for i in range(0,len(message),8):
        blocks.append(message[i:i+8])
    a_init = a
    b_init = b
    c_init = c
    d_init = d
    for block in blocks:
        a,b,c,d = process_round(a,b,c,d,block)
        a3.append(f'{a:0X}')
        b3.append(f'{b:0X}')
        c3.append(f'{c:0X}')
        d3.append(f'{d:0X}')

    a_f ,b_f,c_f,d_f = (a^a_init),(b^b_init),(c^c_init),(d^d_init)
    abcd_f  = f'{a_f:0X}'+ f'{b_f:0X}' + f'{c_f:0X}' + f'{d_f:0X}'
    print(f'H: {abcd_f}')
    return a3,b3,c3,d3

ar,br,cr,dr = process_message(a,b,c,d,message)

print(f'a : {ar}')
print(f'b : {br}')
print(f'c : {cr}')
print(f'd : {dr}')

"""
H: 5073
a : ['E', 'A', 'C', 'D']
b : ['C', '2', '8', '4']
c : ['3', '8', '5', 'C']
d : ['7', 'F', '1', 'F']
SAME AS MEMO
"""