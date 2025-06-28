# Importing the random library to generate random numbers
import random

# Function to calculate the Greatest Common Divisor (GCD) of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to calculate the modular inverse of a number modulo m
def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Function to test if a number is prime (using the Miller-Rabin primality test)
def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Function to generate a potential prime number candidate
def generate_prime_candidate(length):
    p = random.getrandbits(length)
    p |= (1 << length - 1) | 1
    return p

# Function to generate a prime number close to the specified length
def generate_prime(length):
    p = generate_prime_candidate(length)
    while not is_prime(p):
        p = generate_prime_candidate(length)
    return p

# Function to generate RSA keys with a specified key length
def generate_keys(key_length):
    p = generate_prime(key_length // 4)
    q = generate_prime(key_length // 4)
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(2, phi)  # Start from 2 to ensure coprimality with phi
    while gcd(e, phi) != 1:
        e = random.randint(2, phi)

    d = modinv(e, phi)
    return ((e, n), (d, n))

# Function to encrypt a message
def encrypt(m, public_key):
    e, n = public_key
    return pow(m, e, n)

# Function to decrypt a message
def decrypt(c, private_key):
    d, n = private_key
    return pow(c, d, n)

# Function to encode a message into a list of integers representing the ASCII codes of characters
def encode_message(message):
    return [ord(char) for char in message]

# Function to decode a message encoded into a string of characters
def decode_message(encoded_message):
    return ''.join(chr(char) for char in encoded_message)

# This part of the Python program that implements effectively the RSA algorithm, displays the presentation of that Python program (that takes charge of the right choosing of the offered options described below, for the standard key sizes)
print("The present Python program will demonstrate the effectiveness of a right implementation of the RSA asymmetric encryption and decryption algorithm. For that purpose, the implementation of that asymmetric algorithm RSA uses a certain standard key sizes and standard message length determined by international organisations around the world, these standard key sizes and standard message length are the following ones:\n")

print("a: 1024 bits.")
print("b: 2048 bits.")
print("c: 3072 bits.")
print("d: 4096 bits.")
print("e: 7680 bits.")
print("f: 8192 bits.\n")

print("The standard key sizes and standard message length showed above are used by the RSA asymmetric encryption and decryption algorithm for the generation and creation of the public and private keys, and for the calculations related to the encryption and decryption process, that are immense and colossal prime numbers generated randomly. However, for the purpose of the present Python program, these standard key sizes showed out above are used also for specifying the size of the message that must be first encrypted and then decrypted by this RSA asymmetric encryption and decryption algorithm.\n")

print("The present Python program, in order to demonstrate the effectiveness of the right implementation of that RSA asymmetric encryption and decryption algorithm, needs to know which standard key size and which standard message length will be used by the RSA asymmetric encryption and decryption algorithm, taking into account that you must choose one of the following standard key sizes and standard message lengths:\n")

print("a: 1024 bits.")
print("b: 2048 bits.")
print("c: 3072 bits.")
print("d: 4096 bits.")
print("e: 7680 bits.")
print("f: 8192 bits.\n") 

print("For that purpose, please specify and choose a standard message length from the list shown above:")
user_response_standard_message_length = input("Enter your choice (a, b, c, d, e, or f): ")

if user_response_standard_message_length == "a":
    user_response_message_length = 128
elif user_response_standard_message_length == "b":
    user_response_message_length = 256
elif user_response_standard_message_length == "c":
    user_response_message_length = 384
elif user_response_standard_message_length == "d":
    user_response_message_length = 512
elif user_response_standard_message_length == "e":
    user_response_message_length = 960
elif user_response_standard_message_length == "f":
    user_response_message_length = 1024

while user_response_standard_message_length not in {"a", "b", "c", "d", "e", "f"}:
    print("Invalid option. Please choose a valid option (a, b, c, d, e, or f).")
    user_response_standard_message_length = input("Enter your choice (a, b, c, d, e, or f): ")

print("For that purpose, please specify and choose a standard key size from the list shown above:")
user_response_standard_key_size = input("Enter your choice (a, b, c, d, e, or f): ")

if user_response_standard_key_size == "a":
    user_response_key_size = 128*8
elif user_response_standard_key_size == "b":
    user_response_key_size = 256*8
elif user_response_standard_key_size == "c":
    user_response_key_size = 384*8
elif user_response_standard_key_size == "d":
    user_response_key_size = 512*8
elif user_response_standard_key_size == "e":
    user_response_key_size = 960*8
elif user_response_standard_key_size == "f":
    user_response_key_size = 1024*8

while user_response_standard_key_size not in {"a", "b", "c", "d", "e", "f"}:
    print("Invalid option. Please choose a valid option (a, b, c, d, e, or f).")
    user_response_standard_key_size = input("Enter your choice (a, b, c, d, e, or f): ")

# Checking the consistency between the message length and the key size
while True:
    if user_response_standard_message_length == user_response_standard_key_size:
        break
    else:
        print("Error: The selected message length must match the selected key size.")
        print("Please choose the same option (a, b, c, d, e, or f) for both message length and key size.")
        user_response_standard_message_length = input("Enter your choice for message length (a, b, c, d, e, or f): ")
        user_response_standard_key_size = input("Enter your choice for key size (a, b, c, d, e, or f): ")

if user_response_standard_message_length == "a":
    user_response_message_length = 128
elif user_response_standard_message_length == "b":
    user_response_message_length = 256
elif user_response_standard_message_length == "c":
    user_response_message_length = 384
elif user_response_standard_message_length == "d":
    user_response_message_length = 512
elif user_response_standard_message_length == "e":
    user_response_message_length = 960
elif user_response_standard_message_length == "f":
    user_response_message_length = 1024

if user_response_standard_key_size == "a":
    user_response_key_size = 128*8
elif user_response_standard_key_size == "b":
    user_response_key_size = 256*8
elif user_response_standard_key_size == "c":
    user_response_key_size = 384*8
elif user_response_standard_key_size == "d":
    user_response_key_size = 512*8
elif user_response_standard_key_size == "e":
    user_response_key_size = 960*8
elif user_response_standard_key_size == "f":
    user_response_key_size = 1024*8

if user_response_standard_key_size == "a":
    msg = input("Enter a message that contains maximum 128 characters, spaces included: ")
elif user_response_standard_key_size == "b":
    msg = input("Enter a message that contains maximum 256 characters, spaces included: ")
elif user_response_standard_key_size == "c":
    msg = input("Enter a message that contains maximum 384 characters, spaces included: ")
elif user_response_standard_key_size == "d":
    msg = input("Enter a message that contains maximum 512 characters, spaces included: ")
elif user_response_standard_key_size == "e":
    msg = input("Enter a message that contains maximum 960 characters, spaces included: ")
elif user_response_standard_key_size == "f":
    msg = input("Enter a message that contains maximum 1024 characters, spaces included: ")

while len(msg) > user_response_message_length:
    print(f"The message written down has more than {user_response_message_length} characters, including spaces!")
    msg = input(f"Please write down a message that contains {user_response_message_length} characters, including spaces:")

print("Generating RSA keys...")
public_key, private_key = generate_keys(user_response_key_size // 4)
print("RSA keys generated successfully.")

message = msg
encoded_message = encode_message(message)
encrypted_message = [encrypt(char, public_key) for char in encoded_message]
decrypted_message = [decrypt(char, private_key) for char in encrypted_message]
decoded_message = decode_message(decrypted_message)

print("\nInitial message:")
print(message)
print("\nPublic key:")
print(public_key)
print("\nPrivate key:")
print(private_key)
print("\nEncoded message (encrypted by public key):")
print(encrypted_message)
print("\nDecoded message (decrypted by private key):")
print(decoded_message)
