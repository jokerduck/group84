from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
import time
def generate_ecdh_key_pair():
    private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
    public_key = private_key.public_key()
    return private_key, public_key

def derive_shared_secret(private_key, peer_public_key):
    shared_secret = private_key.exchange(ec.ECDH(), peer_public_key)
    return shared_secret

# Alice生成她的密钥对
alice_private_key, alice_public_key = generate_ecdh_key_pair()

# Bob生成他的密钥对
bob_private_key, bob_public_key = generate_ecdh_key_pair()

# Alice从Bob的公钥派生共享密钥
alice_shared_secret = derive_shared_secret(alice_private_key, bob_public_key)

# Bob从Alice的公钥派生共享密钥
bob_shared_secret = derive_shared_secret(bob_private_key, alice_public_key)

# Alice和Bob应该拥有相同的共享密钥
t1=time.time()
print("Alice的共享密钥:", alice_shared_secret.hex())
print("Bob的共享密钥:", bob_shared_secret.hex())

print(time.time()-t1,"s")
