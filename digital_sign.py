import random
import hashlib

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def generate_keypair():
    p = q = 1
    while not is_prime(p):
        p = random.randint(100, 1000)
    while not is_prime(q) or p == q:
        q = random.randint(100, 1000)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(1, phi)
    while gcd(e, phi) != 1:
        e = random.randint(1, phi)
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

def rsa_encrypt(message, public_key):
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

def rsa_decrypt(encrypted_message, private_key):
    d, n = private_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_message])
    return decrypted_message

def generate_signature(message, private_key):
    hashed_message = hashlib.sha256(message.encode()).hexdigest()
    signature = rsa_encrypt(hashed_message, private_key)
    return signature

def verify_signature(message, signature, public_key):
    hashed_message = hashlib.sha256(message.encode()).hexdigest()
    decrypted_signature = rsa_decrypt(signature, public_key)
    return decrypted_signature == hashed_message

# Main program
print("Generating RSA key pair...")
public_key, private_key = generate_keypair()
print("RSA Key Pair Generated.")
print("Public Key:", public_key)
print("Private Key:", private_key)

message = input("Enter the message to be sent: ")

encrypted_message = rsa_encrypt(message, public_key)
signature = generate_signature(message, private_key)

print("\nEncrypted Message:", encrypted_message)
print("Signature:", signature)

# Simulation of transmission
# In a real scenario, the encrypted message and signature would be sent over a network
# For simulation purposes, let's assume that the encrypted message and signature are received by the receiver

received_message = rsa_decrypt(encrypted_message, private_key)
is_signature_valid = verify_signature(received_message, signature, public_key)

print("\nReceived Message:", received_message)
if is_signature_valid:
    print("Signature is valid. Message integrity verified.")
else:
    print("Invalid Signature. Message may have been tampered with.")
