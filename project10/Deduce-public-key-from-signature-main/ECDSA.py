from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.utils import encode_dss_signature, decode_dss_signature

# 生成ECDSA密钥对
def generate_ecdsa_key_pair():
    private_key = ec.generate_private_key(ec.SECP256R1())
    public_key = private_key.public_key()
    return private_key, public_key

# 对数据进行ECDSA签名
def sign_data(private_key, data):
    signature = private_key.sign(data, ec.ECDSA(hashes.SHA256()))
    r, s = decode_dss_signature(signature)
    return encode_dss_signature(r, s)

# 验证ECDSA签名
def verify_signature(public_key, data, signature):
    signature = decode_dss_signature(signature)
    try:
        public_key.verify(signature, data, ec.ECDSA(hashes.SHA256()))
        return True
    except:
        return False

if __name__ == "__main__":
    # 示例用数据
    message = b"Hello, world!"

    # 生成密钥对
    private_key, public_key = generate_ecdsa_key_pair()

    # 对数据进行签名
    signature = sign_data(private_key, message)

    # 验证签名
    is_valid = verify_signature(public_key, message, signature)

    print("Message:", message)
    print("Signature:", signature)
    print("Signature Valid:", is_valid)
