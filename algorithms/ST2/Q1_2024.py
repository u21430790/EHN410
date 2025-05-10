# ANSI X9.17 EDE ROUNDS

#QUESTION 1 [30]
V11= 'FBB36449' #(V1)
K11 = 0x141D2236 #(K1)
K21 = 0xE3BEDAD3 #(K2)
DT1 = ['1640227C','04220141','2E808817','26164484','81A6924D','E5121201','2093202C','84632D45']
DT1_hexint = [0x1640227C,0x04220141,0x2E808817,0x26164484,0x81A6924D,0xE5121201,0x2093202C,0x84632D45] #(DT1 to DT8)

X1 = [] #X1 to X8 (output of first EDE that takes DTi as input) [6]
R1 = [] #R1 to R8 [12] 
V1 = [] #V2 to V8    [12]
"""
MEMO 
#QUESTION 1 [30]
X1_ans = ['C1C2CC93', 'E2FFDEF1', '6BA9F453', 'A73AFCC5', '71F35B75', 'F1BF3FC1', 'C392FA40', 'CEFB5EB0'] #[6]
R1_ans = ['4B64E0A2', '6D3AF7A3', '42FB7B96', 'ECFA1192', '29D8A5C9', '5E87366E', '6C15F350', 'C85AFE86'] #[12]
V1_ans = ['CF8F5075', 'CAEC5516', '6C7BF381', '0EE99113', '1D0282F8', 'EA1175EB', 'EAAE7554', '4388DC72'] #[12]
"""
#Ri = EDE([K1, K2], [Vi ⊕ EDE([K1, K2], DTi)])
#Vi +1 = EDE([K1, K2], [Ri ⊕ EDE([K1, K2], DTi)])


def encrypt_round(input,key):
    left = input[:4]
    right = input[4:]
    new = right+left
    int_new = int(new,16)
     
    return f'{int_new^key:08X}'

def decrypt_round(input1,key): 
    xored =int(input1,16)^key
    xored_bin = f'{xored:08X}'

    left = xored_bin[:4]
    right = xored_bin[4:]
    new = right+left
     
    return new

for D in DT1:
    x  = encrypt_round(D,K11)
    x = decrypt_round(x,K21)
    x = encrypt_round(x,K11)
    X1.append(x)

seed = V11
for x in X1:
    R = f'{int(seed,16) ^ int(x,16):08X}'
    R = encrypt_round(R,K11)
    R = decrypt_round(R,K21)
    R= encrypt_round(R,K11)
    R1.append(R)
    seed =  f'{int(R,16) ^ int(x,16):08X}'
    seed = encrypt_round(seed,K11)
    seed = decrypt_round(seed,K21)
    seed= encrypt_round(seed,K11)
    V1.append(seed)

print(f'X1 : {X1}')
print(f'R1 : {R1}')
print(f'V1 : {V1}')
"""
MATCHES MEMO
X1 : ['C1C2CC93', 'E2FFDEF1', '6BA9F453', 'A73AFCC5', '71F35B75', 'F1BF3FC1', 'C392FA40', 'CEFB5EB0']
R1 : ['4B64E0A2', '6D3AF7A3', '42FB7B96', 'ECFA1192', '29D8A5C9', '5E87366E', '6C15F350', 'C85AFE86']
V1 : ['CF8F5075', 'CAEC5516', '6C7BF381', '0EE99113', '1D0282F8', 'EA1175EB', 'EAAE7554', '4388DC72']
"""