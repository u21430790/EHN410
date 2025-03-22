def encrypt(message,key):
    mes = ""
    for i in range(len(message)):
        mes+= chr((ord(message[i])-97+ ord(key[i])-97)%26+97)
    return mes.upper()

def decrypt(message,key):
    mes = ""
    for i in range(len(message)):
        mes+= chr(((ord(message[i])-97) - (ord(key[i])-97))%26+97)
    return mes

key = "deceptivedeceptivedeceptive"
plaintext="wearediscoveredsaveyourself"

x = encrypt(plaintext,key)
print(x)
y = decrypt(x.lower(),key)
print(y)