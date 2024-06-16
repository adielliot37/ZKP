from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

class EncryptionService:
    def __init__(self):
        self.key = get_random_bytes(16)  

    def encrypt(self, plaintext):
        cipher = AES.new(self.key, AES.MODE_EAX)
        nonce = cipher.nonce
        ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode())
        return base64.b64encode(nonce + tag + ciphertext).decode()

    def decrypt(self, token):
        raw = base64.b64decode(token)
        nonce, tag, ciphertext = raw[:16], raw[16:32], raw[32:]
        cipher = AES.new(self.key, AES.MODE_EAX, nonce=nonce)
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)
        return plaintext.decode()
