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
"""
Phase 1: Key Distribution
1. Receiver sends their RSA public key to Transmitter,
2. Transmitter uses RSA to encrypt a given or generated RC4 key,
3. Transmitter sends the encrypted RC4 key to the Receiver
"""
print(f"RECEIVER p: {r_p}")
print(f"RECEIVER q: {r_q}")

rec = Receiver()
rec.generate_RSA_Keys(r_p,r_q)
#n= 0 # calculate n
#phi = 0 # calculate phi
#recPubKey = 0 # calc pub key
#recPrivKey = 0 # calc private key

print(f"RECEIVER Calculated n: {rec.n}")
print(f"RECEIVER Calculated phi: {rec.phi}")
print(f"RECEIVER Calculated public key: {rec.publicKey}")
print(f"RECEIVER Calculated private key: {rec.privateKey}")

print("\n")

print("TRANSMITTER Please enter RC4 key: ")
tran = Transmitter()
RC4_Key = input()
print(f"TRANSMITTER Given key: {RC4_Key}")
K = RC4_Key.encode('ascii').hex()

RC4_cipher = tran.encrypt_With_RSA(K,rec.publicKey)
recRC4_Key = rec.decrypt_With_RSA(RC4_cipher,rec.privateKey)

print(f"TRANSMITTER Given key in Integers: {K}")
print(f"TRANSMITTER ENCRYPTED RC4 KEY: {RC4_cipher}")
print(f"REEIVER DECRYPTED RC4 key: {recRC4_Key}")

print("\n")
print("PHASE 2")
"""
Phase 2: Data Signing and Encryption
1. Transmitter processes the message stream through a hash function,
2. Transmitter appends the message with its hash to form the digest,
3. Transmitter encrypts the digest stream using RC4,
4. Transmitter sends the encrypted data to the Receiver.
"""
print("\n")
print("TRANSMITTER Please enter a message: ")

message = input()
digest = tran.create_Digest(message)
messageHex,plainHash = rec.split_Digest(digest)

encryptedDigest = tran.encrypt_with_RC4(digest,RC4_Key)
encrHash = tran.encrypt_with_RC4(plainHash,RC4_Key)

print(f"TRANSMITTER Plaintex Hash: {plainHash}")
print(f"TRANSMITTER Encrypted Ciphertext: {encryptedDigest}")
print("\n")

print("PHASE 3")
print("\n")
"""

1. Receiver gets the encrypted ciphertext from Transmitter,
2. Receiver decrypts the data stream using RC4 to get the received digest,
3. Receiver computes the hash for the received message and compares it to the received
hash,
4. The message is authenticated when the hashes match.
3

"""
K1 = bytes.fromhex(recRC4_Key).decode('ascii')
recCipher = rec.decrypt_With_RC4(encryptedDigest,RC4_Key)
messageH,plainhash = rec.split_Digest(recCipher)
plainMessage = sha_Hex_To_Str(messageH)

print(f"RECEIVER Received Ciphertext: {recCipher}")
print("\n")
print(f"RECEIVER Decrypted Message: {plainMessage}")

print("\n")
authentication,mes, recHash,CalcHash = rec.authenticate_Message(recCipher)


print(f"RECEIVER Expected Hash: {CalcHash}")
print(f"RECEIVER Received Hash: {recHash}")
if authentication:
    print("Message Authenticated")
else:
    print("Message unable to be Authenticated")