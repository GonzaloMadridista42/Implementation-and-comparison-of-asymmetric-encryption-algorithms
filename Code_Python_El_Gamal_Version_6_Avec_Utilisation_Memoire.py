# Importing the random library to generate random numbers
import random

# Importing the sys module to increase the recursion limit
import sys  # The sys module provides access to some variables used or maintained by the Python interpreter and to functions that interact strongly with the interpreter.

# importing the psutil library to measure the memory consumption that takes the RSA python code, to perform key generation, encoding and decoding of messages
import psutil

# Function to measure memory usage
def get_memory_usage():
    process = psutil.Process()
    return process.memory_info().rss / 1024  # Convert to kilobytes

# Example of using the function
before_memory = get_memory_usage()

# Increase the recursion limit
sys.setrecursionlimit(10**6)

# Increase the limit for integer string conversion
sys.set_int_max_str_digits(10000)

# To find gcd of two numbers
def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)

# For key generation i.e. large random number
def gen_key(q):
    key = random.randint(pow(2, 900), q)
    while gcd(q, key) != 1:
        key = random.randint(pow(2, 900), q)
    return key

def power(a, b, c):
    x = 1
    y = a
    while b > 0:
        if b % 2 == 0:
            x = (x * y) % c
        y = (y * y) % c
        b = b // 2  # Utilisation de la division entière //
    return x % c

import time

# For asymmetric encryption
def encryption(msg, q, h, g):
    ct = []
    k = gen_key(q)
    s = power(h, k, q)
    p = power(g, k, q)
    for i in range(0, len(msg)):
        ct.append(msg[i])
    for i in range(0, len(ct)):
        ct[i] = s * ord(ct[i])

    return ct, p, s
    
# For decryption
def decryption(ct, p, key, q):
    pt = []
    h = power(p, key, q)
    for i in range(0, len(ct)):
        pt.append(chr(int(ct[i] / h)))
    return pt

# This part of the Python program that implements effectively the El-Gamal algorithm, displays the presentation of that Python program (that takes charge of the right choosing of the offered options described below, for the standard key sizes)
print("The present Python program will demonstrate the effectiveness of a right implementation of the El-Gamal asymmetric encryption and decryption algorithm. For that purpose, the implementation of that asymmetric algorithm El-Gamal uses a certain standard key sizes and standard message length determined by international organisations around the world, these standard key sizes and standard message length are the following ones:\n")

print("a: 2048 bits.")
print("b: 3072 bits.")
print("c: 4096 bits.")
print("d: 6144 bits.")
print("e: 8192 bits.")
print("f: 16384 bits.\n")

print("The standard key sizes and standard message length showed above are used by the El-Gamal asymmetric encryption and decryption algorithm for the generation and creation of the public and private keys, and for the calculations related to the encryption and decryption process, that are immense and colossal prime numbers generated randomly. However, for the purpose of the present Python program, these standard key sizes showed out above are used also for specifying the size of the message that must be first encrypted and then decrypted by this El-Gamal asymmetric encryption and decryption algorithm.\n")

print("The present Python program, in order to demonstrate the effectiveness of the right implementation of that El-Gamal asymmetric encryption and decryption algorithm, needs to know which standard key size and which standard message length will be used by the El-Gamal asymmetric encryption and decryption algorithm, taking into account that you must choose one of the following standard key sizes and standard message lengths:\n")

print("a: 2048 bits.")
print("b: 3072 bits.")
print("c: 4096 bits.")
print("d: 6144 bits.")
print("e: 8192 bits.")
print("f: 16384 bits.\n") 

print("For that purpose, please specify and choose a standard message length from the list shown above:")
user_response_standard_message_length = input("Enter your choice (a, b, c, d, e, or f): ")

if user_response_standard_message_length == "a":
    user_response_message_length = 256
elif user_response_standard_message_length == "b":
    user_response_message_length = 384
elif user_response_standard_message_length == "c":
    user_response_message_length = 512
elif user_response_standard_message_length == "d":
    user_response_message_length = 768
elif user_response_standard_message_length == "e":
    user_response_message_length = 1024
elif user_response_standard_message_length == "f":
    user_response_message_length = 2048

while user_response_standard_message_length not in {"a", "b", "c", "d", "e", "f"}:
    print("Invalid option. Please choose a valid option (a, b, c, d, e, or f).")
    user_response_standard_message_length = input("Enter your choice (a, b, c, d, e, or f): ")

print("For that purpose, please specify and choose a standard key size from the list shown above:")
user_response_standard_key_size = input("Enter your choice (a, b, c, d, e, or f): ")

if user_response_standard_key_size == "a":
    user_response_key_size = 256*8
elif user_response_standard_key_size == "b":
    user_response_key_size = 384*8
elif user_response_standard_key_size == "c":
    user_response_key_size = 512*8
elif user_response_standard_key_size == "d":
    user_response_key_size = 768*8
elif user_response_standard_key_size == "e":
    user_response_key_size = 1024*8
elif user_response_standard_key_size == "f":
    user_response_key_size = 2048*8

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
    user_response_message_length = 256
elif user_response_standard_message_length == "b":
    user_response_message_length = 384
elif user_response_standard_message_length == "c":
    user_response_message_length = 512
elif user_response_standard_message_length == "d":
    user_response_message_length = 768
elif user_response_standard_message_length == "e":
    user_response_message_length = 1024
elif user_response_standard_message_length == "f":
    user_response_message_length = 2048

if user_response_standard_key_size == "a":
    user_response_key_size = 256*8
elif user_response_standard_key_size == "b":
    user_response_key_size = 384*8
elif user_response_standard_key_size == "c":
    user_response_key_size = 512*8
elif user_response_standard_key_size == "d":
    user_response_key_size = 768*8
elif user_response_standard_key_size == "e":
    user_response_key_size = 1024*8
elif user_response_standard_key_size == "f":
    user_response_key_size = 2048*8

if user_response_standard_key_size == "a":
    msg = input("Enter a message that contains maximum 256 characters, spaces included: ")
elif user_response_standard_key_size == "b":
    msg = input("Enter a message that contains maximum 384 characters, spaces included: ")
elif user_response_standard_key_size == "c":
    msg = input("Enter a message that contains maximum 512 characters, spaces included: ")
elif user_response_standard_key_size == "d":
    msg = input("Enter a message that contains maximum 768 characters, spaces included: ")
elif user_response_standard_key_size == "e":
    msg = input("Enter a message that contains maximum 1024 characters, spaces included: ")
elif user_response_standard_key_size == "f":
    msg = input("Enter a message that contains maximum 2048 characters, spaces included: ")

while len(msg) > user_response_message_length:
    print(f"The message written down has more than {user_response_message_length} characters, including spaces!")
    msg = input(f"Please write down a message that contains {user_response_message_length} characters, including spaces:")

if user_response_standard_key_size == "a":
    q=random.randint(pow(2, 900),pow(2, 2048))
elif user_response_standard_key_size == "b":
    q=random.randint(pow(2, 900),pow(2, 3072))
elif user_response_standard_key_size == "c":
    q=random.randint(pow(2, 900),pow(2, 4096))
elif user_response_standard_key_size == "d":
    q=random.randint(pow(2, 900),pow(2, 6144))
elif user_response_standard_key_size == "e":
    q=random.randint(pow(2, 900),pow(2, 8192))
elif user_response_standard_key_size == "f":
    q=random.randint(pow(2, 900),pow(2, 16384))

print("Generating El-Gamal keys...")
g = random.randint(2, q)
key = gen_key(q)
h = power(g, key, q)
print("El-Gamal keys generated successfully.")

print("\ng used=", g)
print("g^a used=", h)

ct, p, s = encryption(msg, q, h, g)
print("g^k used= ", p)
print("g^ak used= ", s)

print("\nOriginal Message=", msg)
print("\nEncrypted Message=", ct)

pt = decryption(ct, p, key, q)
d_msg = ''.join(pt)
print("\nDecrypted Message=", d_msg)

after_memory = get_memory_usage()
memory_used = after_memory - before_memory

if __name__ == '__main__':
    # Code block that measures the memory consumption of the python code implementing the RSA algorithm 
    print("Memory used :", memory_used, "kilobytes")  
