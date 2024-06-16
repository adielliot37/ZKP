import unittest
from src.zkp_module import sign_message, verify_signature

class TestZKPModule(unittest.TestCase):
    def setUp(self):
        self.message = b'ZkAGI proof of knowledge'
        self.priv_key = b'\x01' * 32
        self.pub_key = b'\x02' * 64

    def test_signature_verification(self):
        signature = sign_message(self.message, self.priv_key)
        result = verify_signature(self.message, signature, self.pub_key)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
