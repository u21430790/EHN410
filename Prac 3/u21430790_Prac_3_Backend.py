import numpy as np
from u21430790_Prac_3_RC4 import *

### TEST  DA CODE
def test():
    test_str = "Hi, my name is..."
    test_hex = "48656c6c6f20576f726c64"
    #x = sha_String_To_Hex(test_str)
    #print(x)
    #print(sha_Hex_To_Str(x))
    test_long ="7a6f4f3c2b1a096e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a1908"
    x = sha_Calculate_Hash(test_long)
    print(x)
    return

def sha_Preprocess_Message(inputHex: str) -> str:

    original_length_bits = len(inputHex) * 4
    padded_hex = inputHex + '8'
    current_length_bits = len(padded_hex) * 4
    zero_bits_needed = (896 - (current_length_bits % 1024)) % 1024
    zero_hex_chars = zero_bits_needed // 4
    padded_hex += '0' * zero_hex_chars
    length_hex = format(original_length_bits, '032X')
    padded_hex += length_hex
    
    return padded_hex

def sha_Create_Message_Blocks(inputHex: str) -> np.ndarray:
    length = 1024//4
    blocks = []
    for i in range(0,len(inputHex),length):
         blocks.append(inputHex[i:i+length])
    
    return np.array(blocks)

def sha_Message_Schedule(inputHex: str) -> np.ndarray:
    length = 64//4
    blocks = []
    for i in range(0,len(inputHex),length):
         blocks.append(inputHex[i:i+length])
    
    return np.array(blocks)


def sha_Hash_Round_Function(messageWordHex: str, aHex: str, bHex: str, cHex: str, dHex: str, eHex: str, fHex: str,
                            gHex: str, hHex: str, roundConstantHex: str) -> tuple:
   
    def rightRotate(hex1,shift):
         bin_list = list(bin(hex1)[2:].zfill(64))
         shifted = np.roll(bin_list,shift)
         joined = ''.join(shifted)
         int_ans = int(joined,2)

         return int_ans

    a = int(aHex,16)
    b = int(bHex,16)
    c = int(cHex,16)
    d = int(dHex,16)
    e = int(eHex,16)
    f = int(fHex,16)
    g = int(gHex,16)
    h = int(hHex,16)
    word = int(messageWordHex,16)
    key = int(roundConstantHex,16)


    CHefg =(e & f)^(~e & g)
    MAJabc = (a & b) ^ (a & c) ^ (b & c)
    sigma512a = rightRotate(a,28) ^ rightRotate(a,34)^rightRotate(a,39)
    sigma512e = rightRotate(e,14) ^ rightRotate(e,18)^rightRotate(e,41)
    T1 = (h+ CHefg +sigma512e + word +key) % (2**64)
    T2 = (sigma512a + MAJabc) % (2**64)
    
    h = f'{g:016x}'
    g = f'{f:016x}'
    f = f'{e:016x}'
    e = f'{(d+T1)% (2**64):016x}'
    d = f'{c:016x}'
    c = f'{b:016x}'
    b = f'{a:016x}'
    a = f'{(T1+T2)% (2**64):016x}'

    return a,b,c,d,e,f,g,h



def sha_F_Function(messageBlock: str, aHex: str, bHex: str, cHex: str, dHex: str, eHex: str, fHex: str, gHex: str,
                   hHex: str) -> tuple:
    roundConstants = [
    "428a2f98d728ae22", "7137449123ef65cd", "b5c0fbcfec4d3b2f", "e9b5dba58189dbbc",
    "3956c25bf348b538", "59f111f1b605d019", "923f82a4af194f9b", "ab1c5ed5da6d8118",
    "d807aa98a3030242", "12835b0145706fbe", "243185be4ee4b28c", "550c7dc3d5ffb4e2",
    "72be5d74f27b896f", "80deb1fe3b1696b1", "9bdc06a725c71235", "c19bf174cf692694",
    "e49b69c19ef14ad2", "efbe4786384f25e3", "0fc19dc68b8cd5b5", "240ca1cc77ac9c65",
    "2de92c6f592b0275", "4a7484aa6ea6e483", "5cb0a9dcbd41fbd4", "76f988da831153b5",
    "983e5152ee66dfab", "a831c66d2db43210", "b00327c898fb213f", "bf597fc7beef0ee4",
    "c6e00bf33da88fc2", "d5a79147930aa725", "06ca6351e003826f", "142929670a0e6e70",
    "27b70a8546d22ffc", "2e1b21385c26c926", "4d2c6dfc5ac42aed", "53380d139d95b3df",
    "650a73548baf63de", "766a0abb3c77b2a8", "81c2c92e47edaee6", "92722c851482353b",
    "a2bfe8a14cf10364", "a81a664bbc423001", "c24b8b70d0f89791", "c76c51a30654be30",
    "d192e819d6ef5218", "d69906245565a910", "f40e35855771202a", "106aa07032bbd1b8",
    "19a4c116b8d2d0c8", "1e376c085141ab53", "2748774cdf8eeb99", "34b0bcb5e19b48a8",
    "391c0cb3c5c95a63", "4ed8aa4ae3418acb", "5b9cca4f7763e373", "682e6ff3d6b2b8a3",
    "748f82ee5defb2fc", "78a5636f43172f60", "84c87814a1f0ab72", "8cc702081a6439ec",
    "90befffa23631e28", "a4506cebde82bde9", "bef9a3f7b2c67915", "c67178f2e372532b",
    "ca273eceea26619c", "d186b8c721c0c207", "eada7dd6cde0eb1e", "f57d4f7fee6ed178",
    "06f067aa72176fba", "0a637dc5a2c898a6", "113f9804bef90dae", "1b710b35131c471b",
    "28db77f523047d84", "32caab7b40c72493", "3c9ebe0a15c9bebc", "431d67c49c100d4c",
    "4cc5d4becb3e42b6", "597f299cfc657e2a", "5fcb6fab3ad6faec", "6c44198c4a475817"
    ]

    def rightRotate(hex1,shift):
         bin_list = list(bin(int(hex1,16))[2:].zfill(64))
         shifted = np.roll(bin_list,shift)
         joined = ''.join(shifted)
         int_ans = int(joined,2)

         return int_ans   
    messageSchedule = sha_Message_Schedule(messageBlock)
    words = []
    for t in range(16):
         words.append(messageSchedule[t])
    for t in range(16,80,1):
        sigma1 = (rightRotate(words[t-2],19)^rightRotate(words[t-2],61)^(int(words[t-2],16) >> 6))
        sigma0 = (rightRotate(words[t-15],1)^rightRotate(words[t-15],8)^(int(words[t-15],16) >> 7))
        word = (sigma1 + int(words[t-7],16) +sigma0 + int(words[t-16],16)) % (2**64)
        word = f'{word:016X}'
        words.append(word)
        
        
    for w in range(len(words)):
        aHex,bHex,cHex,dHex,eHex,fHex,gHex,hHex = sha_Hash_Round_Function(words[w],aHex,bHex,cHex,dHex,eHex,fHex,gHex,hHex,roundConstants[w])

    return aHex,bHex,cHex,dHex,eHex,fHex,gHex,hHex


def sha_Process_Message_Block(inputHex: str, aHex: str, bHex: str, cHex: str, dHex: str, eHex: str, fHex: str,
                              gHex: str, hHex: str) -> tuple:
    a_in = int(aHex,16)
    b_in = int(bHex,16)
    c_in = int(cHex,16)
    d_in = int(dHex,16)
    e_in = int(eHex,16)
    f_in = int(fHex,16)
    g_in = int(gHex,16)
    h_in = int(hHex,16)

    aHex,bHex,cHex,dHex,eHex,fHex,gHex,hHex = sha_F_Function(inputHex,aHex,bHex,cHex,dHex,eHex,fHex,gHex,hHex)

    a = int(aHex,16)
    b = int(bHex,16)
    c = int(cHex,16)
    d = int(dHex,16)
    e = int(eHex,16)
    f = int(fHex,16)
    g = int(gHex,16)
    h = int(hHex,16)

    a_f = (a_in+a)%(2**64)
    b_f = (b_in+b)%(2**64)
    c_f = (c_in+c)%(2**64)
    d_f = (d_in+d)%(2**64)
    e_f = (e_in+e)%(2**64)
    f_f = (f_in+f)%(2**64)
    g_f = (g_in+g)%(2**64)
    h_f = (h_in+h)%(2**64)

    a_ = f'{a_f:016X}'
    b_ = f'{b_f:016X}'
    c_ = f'{c_f:016X}'
    d_ = f'{d_f:016X}'
    e_ = f'{e_f:016X}'
    f_ = f'{f_f:016X}'
    g_ = f'{g_f:016X}'
    h_ = f'{h_f:016X}'
    return a_,b_,c_,d_,e_,f_,g_,h_

def sha_Calculate_Hash(inputHex: str) -> str:
    processed = sha_Preprocess_Message(inputHex)
    blocks = sha_Create_Message_Blocks(processed)
    
    h0 = "6a09e667f3bcc908"
    h1 = "bb67ae8584caa73b"
    h2 = "3c6ef372fe94f82b"
    h3 = "a54ff53a5f1d36f1"
    h4 = "510e527fade682d1"
    h5 = "9b05688c2b3e6c1f"
    h6 = "1f83d9abfb41bd6b"
    h7 = "5be0cd19137e2179"
    for b in blocks:

         h0,h1,h2,h3,h4,h5,h6,h7= sha_Process_Message_Block(b,h0,h1,h2,h3,h4,h5,h6,h7)
         
    return h0+h1+h2+h3+h4+h5+h6+h7

def sha_String_To_Hex(inputStr: str) -> str:
    ordArr = [ord(s) for s in inputStr]
    hexStr = ""
    for o in ordArr:
        hexStr+= f'{o:02X}'
    return hexStr


def sha_Image_To_Hex(inputImg: np.ndarray) -> str:
    img = inputImg.flatten()
    hexStr = ""
    for i in img:
        hexStr+= f"{i:02X}"
    return hexStr
def sha_Hex_To_Str(inputHex: str) -> str:
    chrStr = ""
    for i in range(0,len(inputHex),2):
         chrStr+= chr(int(inputHex[i:i+2],16))

    return chrStr


def sha_Hex_To_Im(inputHex: str, originalShape: tuple) -> np.ndarray:
    byte_values = [int(inputHex[i:i+2], 16) for i in range(0, len(inputHex), 2)]
    arr = np.array(byte_values, dtype=np.uint8)
    reshaped_array = arr.reshape(originalShape)
    
    return reshaped_array

class Transmitter:
    def __init__(self, ):
        return

    def encrypt_With_RSA(self, message: str, RSA_Key: tuple) -> np.ndarray:
            key = RSA_Key[0]
            n = RSA_Key[1]
            cipher = [pow(c,key,n) for c in message]
            return cipher

    def create_Digest(self, message) -> str:
            if isinstance(message,str):
                 hexStr = sha_String_To_Hex(message)
                 digest = sha_Calculate_Hash(hexStr)
                 return digest
            
            if isinstance(message, np.ndarray):
                 hexStr = sha_Image_To_Hex(message)
                 digest = sha_Calculate_Hash(hexStr)
                 return digest
            
    def encrypt_with_RC4(self, digest: str, key: str) -> np.ndarray:
            return rc4_Encrypt_String(digest,key)


class Receiver:
    def __init__(self, ):
        self.p = 0
        self.q = 0
        self.n = 0
        self.phi = 0
        self.e = 0
        self.d = 0
        self.publicKey = (0, 0)
        self.privateKey = (0, 0)

    def generate_RSA_Keys(self, newP: int, newQ: int):
            raise Exception("Not Implemented.")

    def decrypt_With_RSA(self, message: np.ndarray, RSA_Key: tuple) -> str:
            key = RSA_Key[0]
            n = RSA_Key[1]
            plaintext = [pow(c,key,n) for c in message]
            return plaintext

    def decrypt_With_RC4(self, digest: np.ndarray, key: str) -> str:
            return rc4_Decrypt_String(digest, key)

    def split_Digest(self, digest: str) -> tuple:
            raise Exception("Not Implemented.")


    def authenticate_Message(self, digest: str) -> tuple:
            raise Exception("Not Implemented.")


test()