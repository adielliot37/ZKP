from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt_data(data, key):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data.encode())
    return nonce, ciphertext, tag

def decrypt_data(nonce, ciphertext, tag, key):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    return data.decode()

def zynapse_fhe_demo():
    key = get_random_bytes(16)  # AES key
    data = "ZkAGI"
    nonce, ciphertext, tag = encrypt_data(data, key)
    decrypted_data = decrypt_data(nonce, ciphertext, tag, key)
    print(f"Decrypted: {decrypted_data}")

if __name__ == "__main__":
    zynapse_fhe_demo()
