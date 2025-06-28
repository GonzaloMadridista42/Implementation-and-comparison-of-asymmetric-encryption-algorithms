# Importing the random library to generate random numbers
import random

# Importing the sys module to increase the recursion limit
import sys  # The sys module provides access to some variables used or maintained by the Python interpreter and to functions that interact strongly with the interpreter.

# importing the psutil library to measure the memory consumption that takes the RSA python code, to perform key generation, encoding and decoding of messages
import psutil

# importing the time library to measure the time that takes the RSA oython code, to perform key generation, encoding and decoding of messages
import time

# Importing the math library to calculate the size of the generated public and private El-Gamal keys
import math

# Function to measure memory usage
def get_memory_usage():
    process = psutil.Process()
    return process.memory_info().rss / 1024  # Convert to kilobytes

# Example of using the function
before_memory = get_memory_usage()

# Increase the recursion limit
sys.setrecursionlimit(10**6)

# To find gcd of two numbers
def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)

# Function to generate the public and the private keys, for encryption and decryption of messages
def gen_key(q):
    key = random.randint(1, q - 1)
     # Generate a key in the range [1, q - 1]
    while gcd(q, key) != 1:
        key = random.randint(1, q - 1)  # Regenerate key until gcd(q, key) == 1
    
    # Calculate key sizes
    public_key_size = key.bit_length() 
    private_key_size = q.bit_length()  
    
    return key, q, public_key_size, private_key_size  # Return key, q, and key sizes as a tuple

def power(a, b, c):
    x = 1
    y = a
    while b > 0:
        if b % 2 == 0:
            x = (x * y) % c
        y = (y * y) % c
        b = b // 8  # Utilisation de la division entière //
    
    return x % c

# For asymmetric encryption
def encryption(msg, q, h, g):
    ct = []
    k, _, public_key_size, private_key_size = gen_key(q)
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

before_memory = get_memory_usage()
print("Generating El-Gamal keys...")
g = random.randint(2, q)
key, q, public_key_size, private_key_size = gen_key(q)
h = power(g, key, q)
print("El-Gamal keys generated successfully.")

after_memory = get_memory_usage()
memory_used = after_memory - before_memory

print("\ng used=", g)
print("g^a used=", h)

ct, p, s = encryption(msg, q, h, g)
print("g^k used= ", p)
print("g^ak used= ", s)

print("\nOriginal Message: ", msg)
print("\nEncrypted Message: ", ct)

pt = decryption(ct, p, key, q)
d_msg = ''.join(pt)
print("\nDecrypted Message: ", d_msg)

after_memory = get_memory_usage()
memory_used = after_memory - before_memory

# Measurement of the complexity of the key generation operation
def measure_key_generation(q):
    start_memory = get_memory_usage()
    start_time = time.time()
    g = random.randint(2, q)
    key, q, public_key_size, private_key_size = gen_key(q)
    h = power(g, key, q)
    end_time = time.time()
    end_memory = get_memory_usage()
    return end_time - start_time, end_memory - start_memory

# Measurement of the complexity of the encryption operation
def measure_encryption(message, q, h, g):
    start_time = time.time()
    ct, p, s = encryption(message, q, h, g)
    end_time = time.time()
    return end_time - start_time

# Measurement of the complexity of the decryption operation
def measure_decryption(ct, p, key, q):
    start_time = time.time()
    pt = decryption(ct, p, key, q)
    end_time = time.time()
    return end_time - start_time

# Function to generate a message of a given length
def generate_message(user_response_message_length):
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(user_response_message_length))

# Function to generate 5 messages of the same length as the provided plaintext message
def generate_test_messages(message, num_messages):
    return [generate_message(len(message)) for _ in range(num_messages)]

# Function to measure memory usage
def measure_memory_usage():
    process = psutil.Process()
    memory_usage_kb = process.memory_info().rss / 1024  # Convert to kilobytes
    if memory_usage_kb < 0.001:  # If memory usage is very low
        return 0.0000001  # Display a value very close to zero
    else:
        return memory_usage_kb

def calculate_avalanche_effect(key1, key2):
    # Check if key2 is already an integer
    if isinstance(key2, int):
        key2_int = key2
    else:
        key2_int = int(''.join(map(str, key2)))

    # Extract integers from the tuples
    key1_int = int(''.join(map(str, key1)))

    # Calculate the number of different bits between the two keys
    diff_bits = bin(key1_int ^ key2_int).count('1')

    # Calculate the percentage of avalanche effect
    total_bits = max(key1_int.bit_length(), key2_int.bit_length())
    avalanche_percentage = (diff_bits / total_bits) * 100

    return avalanche_percentage

def select_random_digit(key_tuple):
    # Convert each integer in the tuple to a string
    key_str = ''.join(map(str, key_tuple))

    # Select a random digit position
    digit_position = random.randint(0, len(key_str) - 1)

    # Return the selected digit
    return key_str[digit_position]

def modify_key(key, random_digit):
    # Convert the key to a string
    key_str = str(key)
    
    # Generate a random digit position
    digit_position = random.randint(0, len(key_str) - 1)
    
    # Create a list from the string
    key_list = list(key_str)
    
    # Modify the digit at the random position with the provided random digit
    key_list[digit_position] = str(random_digit)
    
    # Convert the modified list back to a string
    modified_key_str = ''.join(key_list)
    
    # Convert the modified string back to an integer
    modified_key = int(modified_key_str)
    
    return modified_key, digit_position

if __name__ == '__main__':
    # Code block that measures the avalanche effect generated by the original public and private keys generated the very first time, then measures the avalanche effect generated by the modified public and private keys bit only one bit for each key, in both cases, this main measures the avalanche effect linked to the keys generation, encryption and decryption of clear and plain messages.
    # Check if keys have already been generated
    if 'g' not in globals() or 'key' not in globals():
        # If keys have not been generated, generate a new key pair using the initial message
        key, q, public_key_size, private_key_size = gen_key(q)
        g = random.randint(2, q)
        h = power(g, key, q)
    else:
        # If keys already exist, retrieve the existing keys
        pass
    
    print("")

    # Print the initial message
    print("Initial Message:")
    print(msg)
    print()

    # Print the initial message length
    message_length = len(msg)  # Length of the initial message
    print(f"Initial message length (including spaces): {message_length} characters")

    # Print the content of the public and the private keys
    print(f"Public key (g) content (unchanged public key): {g}")
    print(f"Public key (h) content (unchanged public key): {h}")
    print(f"Private key (g^k) content (unchanged public key): {p}")
    print(f"Private key (g^ak) content (unchanged public key): {s}")

    # Print the length of the public and the private keys
    print(f"Public key (g) length (unchanged public key): {g.bit_length()} bits")
    print(f"Public key (h) length (unchanged public key): {h.bit_length()} bits")
    print(f"Private key (g^k) length (unchanged public key): {p.bit_length()} bits")
    print(f"Private key (g^ak) length (unchanged public key): {s.bit_length()} bits")

    # Encryption of the initial message using El-Gamal
    ct, p, s = encryption(msg, q, h, g)
    print(f"\nEncrypted initial message (unchanged public and private keys): {ct}")

    # Decryption of the initial message using El-Gamal
    pt = decryption(ct, p, key, q)
    d_msg = ''.join(pt)
    print(f"Decrypted initial message (unchanged public and private keys): {d_msg}")    

    # Calculate the avalanche effect for the public key
    public_key_avalanche_percentage = calculate_avalanche_effect((g, h), public_key_size)

    # Calculate the avalanche effect for the private key
    private_key_avalanche_percentage = calculate_avalanche_effect((p, s), private_key_size)

    # Display the avalanche effect percentages
    print("\nAvalanche Effect for Public Key in % (unchanged public and private keys):", public_key_avalanche_percentage)
    print("Avalanche Effect for Private Key in % (unchanged public and private keys):", private_key_avalanche_percentage)

    # Select and display a random digit from the public key components
    public_random_digit_g = select_random_digit((g,))
    public_random_digit_h = select_random_digit((h,))
    print(f"\nRandom digit from Public Key (g): {public_random_digit_g}")
    print(f"Random digit from Public Key (h): {public_random_digit_h}")

    # Select and display a random digit from the private key components
    private_random_digit_p = select_random_digit((p,))
    private_random_digit_s = select_random_digit((s,))
    print(f"Random digit from Private Key (g^k): {private_random_digit_p}")
    print(f"Random digit from Private Key (g^ak): {private_random_digit_s}")
    
    # Convert the random digit positions to integers
    public_random_digit_g = int(public_random_digit_g)
    public_random_digit_h = int(public_random_digit_h)
    private_random_digit_p = int(private_random_digit_p)
    private_random_digit_s = int(private_random_digit_s)

    # Modify the public and private keys
    modified_public_key_g = modify_key(g, public_random_digit_g)
    modified_public_key_h = modify_key(h, public_random_digit_h)
    modified_private_key_p = modify_key(p, private_random_digit_p)
    modified_private_key_s = modify_key(s, private_random_digit_s)

    # Print the content of the modified public and private keys
    print(f"Public key (g) content (modified public key): {modified_public_key_g}")
    print(f"Public key (h) content (modified public key): {modified_public_key_h}")
    print(f"Private key (g^k) content (modified public key): {modified_private_key_p}")
    print(f"Private key (g^ak) content (modified public key): {modified_private_key_s}")

    # Print the length of the modified public and private keys
    # Get the number of bits for modified_public_key_g
    modified_public_key_g_bits = modified_public_key_g[0].bit_length()

    # Get the number of bits for modified_public_key_h
    modified_public_key_h_bits = modified_public_key_h[0].bit_length()

    # Get the number of bits for modified_private_key_p
    modified_private_key_p_bits = modified_private_key_p[0].bit_length()

    # Get the number of bits for modified_private_key_s
    modified_private_key_s_bits = modified_private_key_s[0].bit_length()

    # Display the results
    print(f"Modified Public key g length: {modified_public_key_g_bits} bits")
    print(f"Modified Public key h length: {modified_public_key_h_bits} bits")
    print(f"Modified Private key p length: {modified_private_key_p_bits} bits")
    print(f"Modified Private key s length: {modified_private_key_s_bits} bits")

    # Encryption of the initial message using the modified public key
    encrypted_modified_public_key = [encryption(char, q, h, g) for char in msg]
    print(f"\nEncrypted initial message (modified public key): {encrypted_modified_public_key}")

    # Decryption of the initial message using the modified private key
    decrypted_modified_private_key = [decryption(char[0], char[1], key, q) for char in encrypted_modified_public_key]
    decoded_modified_private_key_message = ''.join([char[0] for char in decrypted_modified_private_key])  # Extract the first element from each tuple
    print(f"Decrypted initial message (modified private key): {decoded_modified_private_key_message}")

    # Calculate the avalanche effect for the modified public key
    modified_public_key_avalanche_percentage = calculate_avalanche_effect((g,), public_key_size)

    # Calculate the avalanche effect for the modified private key
    modified_private_key_avalanche_percentage = calculate_avalanche_effect((p,), private_key_size)

    # Display the avalanche effect percentages for the modified keys
    print("\nAvalanche Effect for Modified Public Key in % (modified public and private keys):", modified_public_key_avalanche_percentage)
    print("Avalanche Effect for Modified Private Key in % (modified public and private keys):", modified_private_key_avalanche_percentage)