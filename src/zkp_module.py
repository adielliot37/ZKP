from py_ecc.secp256k1 import ecdsa_raw_sign, ecdsa_raw_recover

def sign_message(message, priv_key):
    signature = ecdsa_raw_sign(message, priv_key)
    return signature

def verify_signature(message, signature, pub_key):
    return ecdsa_raw_recover(message, signature) == pub_key

def zynapse_zkp_demo():
    message = b'ZkAGI proof of knowledge'
    priv_key = b'\x01' * 32  
    pub_key = b'\x02' * 64  
    signature = sign_message(message, priv_key)
    valid = verify_signature(message, signature, pub_key)
    print("Signature valid:", valid)

if __name__ == "__main__":
    zynapse_zkp_demo()
