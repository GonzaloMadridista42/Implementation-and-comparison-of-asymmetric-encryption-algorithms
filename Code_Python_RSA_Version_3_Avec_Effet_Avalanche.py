# Importing the random library to generate random numbers
import random

# Importing the psutil library to measure the memory consumption that takes the RSA python code, to perform key generation, encoding and decoding of messages
import psutil

# importing the time library to measure the time that takes the RSA oython code, to perform key generation, encoding and decoding of messages
import time

# Importing the math library to calculate the size of the generated public and private RSA keys
import math

# Function to measure memory usage
def get_memory_usage():
    process = psutil.Process()
    return process.memory_info().rss / 1024  # Convert to kilobytes

# Example of using the function
before_memory = get_memory_usage()

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

# Function to generate the public and the private keys, for encryption and decryption of messages
def generate_keys(key_length):
    p = generate_prime(key_length // 8)
    q = generate_prime(key_length // 8)
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(2, phi)  # Start from 2 to ensure coprimality with phi
    while gcd(e, phi) != 1:
        e = random.randint(2, phi)

    d = modinv(e, phi)
    
    # Calculate key sizes
    public_key_size = n.bit_length()
    private_key_size = d.bit_length()

    return ((e, n), (d, n), public_key_size, private_key_size)

# Function to encrypt a message
def encrypt(m, public_key):
    e, n = public_key
    return pow(m, e, n)

# Function to decrypt a message
def decrypt(c, private_key):
    d, n = private_key
    return pow(int(c), int(d), int(n))

# Function to encode a message into a list of integers representing the ASCII codes of characters
def encode_message(message):
    return [ord(char) for char in message]

# Function to decode a message encoded into a list of integers representing the ASCII codes of characters
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
(public_key, private_key, public_key_size, private_key_size) = generate_keys(user_response_key_size // 4)
print("RSA keys generated successfully.")

before_memory = get_memory_usage()
message = msg
encoded_message = encode_message(message)
encrypted_message = [encrypt(char, public_key) for char in encoded_message]
decrypted_message = [decrypt(char, private_key) for char in encrypted_message]
decoded_message = decode_message(decrypted_message)

after_memory = get_memory_usage()
memory_used = after_memory - before_memory

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

after_memory = get_memory_usage()
memory_used = after_memory - before_memory

# Measurement of the complexity of the key generation operation
def measure_key_generation(key_length):
    start_memory = get_memory_usage()
    start_time = time.time()
    generate_keys(key_length // 4)
    end_time = time.time()
    end_memory = get_memory_usage()
    return end_time - start_time, end_memory - start_memory

# Measurement of the complexity of the encryption operation
def measure_encryption(message, public_key):
    start_time = time.time()
    encrypt(message, public_key)
    end_time = time.time()
    return end_time - start_time

# Measurement of the complexity of the decryption operation
def measure_decryption(encrypted_message, private_key):
    start_time = time.time()
    decrypt(encrypted_message, private_key)
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

#Function to calculate the avalanche effect occurred just by changing the value of a single bit in a given message
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

# Function to randomly select a single bit of a given message, in order to change its value, for eventually measuring the avalanche effect caused by the change of the original value of that bit
def select_random_digit(key_tuple):
    # Convert each integer in the tuple to a string
    key_str = ''.join(map(str, key_tuple))

    # Select a random digit position
    digit_position = random.randint(0, len(key_str) - 1)

    # Return the selected digit
    return key_str[digit_position]

# Function to generate a new public and a new private key, using the firstly generated public and private keys, created by the first compilation of the RSA python code
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
    # Code block that measures the avalanche effect generated by the original public and private keys generated the very first time, then measures the avalanche effect generated by the modified public and private keys bit only one bit for each key, in both cases, this main class measures the avalanche effect linked to the keys generation, encryption and decryption of clear and plain messages.
    # Check if keys have already been generated
    if 'public_key' not in globals() or 'private_key' not in globals():
        # If keys have not been generated, generate a new key pair using the initial message
        encoded_initial_message = encode_message(message)
        public_key, private_key = generate_keys(len(encoded_initial_message))
    else:
        # If keys already exist, retrieve the existing keys
        pass
    
    print("")

    # Print the initial message
    print("Initial Message:")
    print(message)
    print()

    # Print the initial message length
    message_length = len(message)  # Length of the initial message
    print(f"Initial message length (including spaces): {message_length} characters")
    
    # Print the content of the public and the private keys
    print(f"Public key content (unchanged public key): {public_key}")
    print(f"Private key content (unchanged public key): {private_key}")

    # Print the public and private key lengths
    print(f"Public key length (unchanged public key): {public_key_size*2} bits")
    print(f"Private key length (unchanged private key): {private_key_size*2} bits")
    print()

    # Encoding the initial message into a list of integers representing the ASCII codes of characters
    encoded_initial_message = encode_message(message)

    # Encryption of the initial message
    encrypted_initial_message = [encrypt(char, public_key) for char in encoded_initial_message]
    print(f"\nEncrypted initial message (unchanged public and private keys): {encrypted_initial_message}")

    # Decryption of the initial message
    decrypted_initial_message = [decrypt(char, private_key) for char in encrypted_initial_message]
    decoded_initial_message = decode_message(decrypted_initial_message)
    print(f"Decrypted initial message (unchanged public and private keys): {decoded_initial_message}")

    # Calculate the avalanche effect for the public key
    public_key_avalanche_percentage = calculate_avalanche_effect(public_key, public_key_size)

    # Calculate the avalanche effect for the private key
    private_key_avalanche_percentage = calculate_avalanche_effect(private_key, private_key_size)

    # Display the avalanche effect percentages
    print("\nAvalanche Effect for Public Key in % (unchanged public and private keys):", public_key_avalanche_percentage)
    print("Avalanche Effect for Private Key in % (unchanged public and private keys):", private_key_avalanche_percentage)

    # Select and display a random digit from the public key
    public_random_digit = select_random_digit(public_key)
    print(f"\nRandom digit from Public Key: {public_random_digit}")

    # Select and display a random digit from the private key
    private_random_digit = select_random_digit(private_key)
    print(f"Random digit from Private Key: {private_random_digit}")    
    
    # Convert the random digit positions to integers if they are strings
    public_random_digit = int(public_random_digit)
    private_random_digit = int(private_random_digit)

    # Extract the values from the tuples
    public_key_int = int(''.join(map(str, public_key)))
    private_key_int = int(''.join(map(str, private_key)))

    # Modify the public and private keys
    modified_public_key = modify_key(public_key_int, public_random_digit)
    modified_private_key = modify_key(private_key_int, private_random_digit)
    
    # Print the content of the modified public and private keys
    print(f"Public key content (changed public key): {modified_public_key}")
    print(f"Private key content (changed private key): {modified_private_key}")

    # Print the length of the modified public and private keys
    # Get the modified public key value from the tuple
    modified_public_key_value = modified_public_key[0]

    # Get the number of bits for the modified public key
    modified_public_key_bits = modified_public_key_value.bit_length()

    # Get the modified private key value from the tuple  
    modified_private_key_value = modified_private_key[0]

    # Get the number of bits for the modified private key
    modified_private_key_bits = modified_private_key_value.bit_length()

    # Display the results
    print(f"Modified Public key length: {modified_public_key_bits} bits")
    print(f"Modified Private key length: {modified_private_key_bits} bits")   

    # Encryption of the initial message using the modified public key
    encrypted_modified_public_key = [encrypt(char, public_key) for char in encoded_initial_message]
    print(f"\nEncrypted initial message (modified public key): {encrypted_modified_public_key}")

    # Decryption of the initial message using the modified private key
    decrypted_modified_private_key = [decrypt(char, private_key) for char in encrypted_initial_message]
    decoded_modified_private_key_message = decode_message(decrypted_modified_private_key)
    print(f"Decrypted initial message (modified private key): {decoded_modified_private_key_message}") 

    # Calculate the avalanche effect for the modified public key
    modified_public_key_avalanche_percentage = calculate_avalanche_effect(public_key, public_key_size)

    # Calculate the avalanche effect for the modified private key
    modified_private_key_avalanche_percentage = calculate_avalanche_effect(private_key, private_key_size)

    # Display the avalanche effect percentages for the modified keys
    print("\nAvalanche Effect for Modified Public Key in % (modified public and private keys):", modified_public_key_avalanche_percentage)
    print("Avalanche Effect for Modified Private Key in % (modified public and private keys):", modified_private_key_avalanche_percentage)
