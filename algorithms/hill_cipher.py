import numpy as np
from icecream import ic

message = "ACT"
key = "GYBNQKURP"

def hill_encrypt(key,message):
    key_matrix = np.zeros((3,3))
    message_converted = []
    for x in message:
        message_converted.append(ord(x.lower()) - ord('a'))
    
    
    #ic(message_converted)
ic(hill_encrypt(key,message))

