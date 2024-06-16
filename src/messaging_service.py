from .encryption_module import EncryptionService
from .zkp_module import ZKPService

class MessagingService:
    def __init__(self, zkp_private_key):
        self.encryption = EncryptionService()
        self.zkp = ZKPService(zkp_private_key)

    def send_message(self, message):
        encrypted_message = self.encryption.encrypt(message)
        signature = self.zkp.sign(message)
        return encrypted_message, signature

    def receive_message(self, encrypted_message, signature):
        decrypted_message = self.encryption.decrypt(encrypted_message)
        if self.zkp.verify(decrypted_message, signature):
            return decrypted_message
        else:
            return "Verification Failed"
