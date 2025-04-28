def encrypt(message,shift):
    mes = ""
    for m in message:
        
        if (ord(m)-97) <26 - shift:
            mes+= chr(ord(m)+shift %26)
        else:
            
            mes+= chr(ord(m)-26+shift%26)
    return mes

def decrypt(message,shift):
    mes=""
    for m in message:
        print(ord(m)-97)
        if (ord(m)-97) >shift-1:
            mes+= chr(ord(m)-shift %26)
        else:
            
            mes+= chr(ord(m)+26-shift%26)
    return mes

plaintext = "abcdefghijklmnopqrstuvwxyz"
shift = 3
x = encrypt(plaintext,shift)
print(x)
y = decrypt(x,shift)
print(y)