from u21430790_Prac_3_Backend import *

# implement the simulator here.
print("Welcome.")
print("To start a secure transmission channel,")

print("Enter RECEIVER's p value:")
r_p = int(input())
print("Enter RECEIVER's q values:")
r_q = int(input())

print("\n")
print("PHASE 1")
print("\n")

print(f"RECEIVER p: {r_p}")
print(f"RECEIVER q: {r_q}")

n= 0 # calculate n
phi = 0 # calculate phi
recPubKey = 0 # calc pub key
recPrivKey = 0 # calc private key

print(f"RECEIVER Calculated n: {n}")
print(f"RECEIVER Calculated phi: {phi}")
print(f"RECEIVER Calculated public key: {recPubKey}")
print(f"RECEIVER Calculated private key: {recPrivKey}")

print("\n")

print("TRANSMITTER Please enter RC4 key: ")
RC4_Key = input()
RC4_cipher = []
recRC4_Key = 0

print(f"TRANSMITTER Given key: {RC4_Key}")
print(f"TRANSMITTER ENCRYPTED RC4 KEY: {RC4_cipher}")
print(f"REEIVER DECRYPTED RC4 key: {recRC4_Key}")

print("\n")
print("PHASE 2")
print("\n")
print("TRANSMITTER Please enter a message: ")

message = input()
plainHash = ""
encrHash = []
print(f"TRANSMITTER Plaintex Hash: {plainHash}")
print(f"TRANSMITTER Encrypted Ciphertext: {encrHash}")
print("\n")

print("PHASE 3")
print("\n")

recCipher = ""
decCipher = ""
print(f"RECEIVER Received Ciphertext: {recCipher}")
print("/n")
print(f"RECEIVER Decrypted Message: {decCipher}")

print("/n")
exp_Hash =""
recHash = ""

print(f"RECEIVER Expected Hash: {exp_Hash}")
print(f"RECEIVER Received Hash: {recHash}")
if exp_Hash == recHash:
    print("Message Authenticated")
else:
    print("Message unable to be Authenticated")