import numpy as np
nonce1 = 0x039480B2
K1 = 0xFE342A2C


def encrypt(plaintext,key):
    plaintext = list(bin(plaintext)[2:].zfill(32))
    key  = list(bin(key)[2:].zfill(32))
    rolled_plain = np.roll(plaintext,-1)
    rolled_k = np.roll(key,1)

    int_plain = ''.join(rolled_plain)
    int_k = ''.join(rolled_k)
    result = int(int_plain,2)^ int(int_k,2)

    return result

P11 = '538220869CAB2014180A892A9000A321CCA14386'
C12 = 'AE7704B90FF97DB26BC37933ACC44CF53EA6F4EC'

p_blocks = []
for i in range(0,len(P11),8):
    p_blocks.append(P11[i:i+8])

def ofb_encrypt(plaintext_blocks,nonce,key):
    feedback = nonce
    cipher_blocks = []
    for block in plaintext_blocks:
        temp_feedback = feedback
        for i in range(5):
            temp_feedback = encrypt(temp_feedback,key)
                # XOR with plaintext block to get ciphertext
        ciphertext_block = int(block,16) ^ temp_feedback
        cipher_blocks.append(f'{ciphertext_block:0X}')
        
        # Update feedback for next block
        feedback = temp_feedback
    return cipher_blocks

x = ofb_encrypt(p_blocks,nonce1,K1)
print(x)
