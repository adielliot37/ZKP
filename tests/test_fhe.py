import unittest
from src.fhe_module import encrypt_data, decrypt_data
from Crypto.Random import get_random_bytes

class TestFHEModule(unittest.TestCase):
    def test_encryption_decryption(self):
        key = get_random_bytes(16)
        data = "Test data"
        nonce, ciphertext, tag = encrypt_data(data, key)
        decrypted_data = decrypt_data(nonce, ciphertext, tag, key)
        self.assertEqual(decrypted_data, data)

if __name__ == '__main__':
    unittest.main()
