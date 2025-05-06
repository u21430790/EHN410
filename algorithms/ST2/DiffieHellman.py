# CORRECT


def get_key(Ya, Yb, alpha, q):
    # get Xa
    Xa = -1
    for i in range(q):
        if pow(alpha,i) % q == Ya:
            Xa = i
            break
    
    # get the symmetric key
    return pow(Yb,Xa) % q


q = 29
alpha = 11
Ya = 5
Yb = 12

# to get the symmetric key, need Xa
# to get Xa, need Ya, alpha, q (which we have)

k = get_key(Ya,Yb, alpha, q)
print(k)
print((bin(k)[2:].zfill(8))*4)
k = (bin(k)[2:].zfill(8))*4
k = f'{int(k,16):0X}'
c = "385D1F04"

plaintext = (int(c,16)*pow(int(k,16),-1)) % q
print(plaintext)
x = f'{plaintext:0X}'
print(x)