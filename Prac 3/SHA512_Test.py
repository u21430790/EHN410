import hashlib

def sha512_from_hex(hex_str):
    # Convert hex string to bytes
    try:
        byte_data = bytes.fromhex(hex_str)
    except ValueError:
        raise ValueError("Invalid hex string.")

    # Create SHA-512 hash object and update with byte data
    sha512_hash = hashlib.sha512()
    sha512_hash.update(byte_data)

    # Return hexadecimal digest
    return sha512_hash.hexdigest()

# Example usage
if __name__ == "__main__":
    # Sample hex string (you can replace this with your test cases)
    test_hex = "48656c6c6f20576f726c64"  # "Hello World" in hex
    test_long = "7a6f4f3c2b1a096e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a19087f6e5d4c3b2a1908"
    # Compute and print SHA-512 hash
    hash_result = sha512_from_hex(test_long)
    print(f"SHA-512 hash of hex string '{test_long}':\n{hash_result}")
