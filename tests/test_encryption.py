import unittest
from src.encryption_module import EncryptionService

class TestEncryptionService(unittest.TestCase):
    def setUp(self):
        self.encryption_service = EncryptionService()

    def test_encrypt_decrypt(self):
        message = "ZM!, ZkAGI!"
        encrypted = self.encryption_service.encrypt(message)
        decrypted = self.encryption_service.decrypt(encrypted)
        self.assertEqual(decrypted, message)

if __name__ == '__main__':
    unittest.main()
