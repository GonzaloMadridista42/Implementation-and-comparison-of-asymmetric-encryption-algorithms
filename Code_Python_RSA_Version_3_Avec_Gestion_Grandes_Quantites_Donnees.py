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
public_key, private_key = generate_keys(user_response_key_size // 4)
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
    return process.memory_info().rss / 1024  # Convert to kilobytes

if __name__ == '__main__':
    # Code block that measures the algorithmic complexity of the keys generated and the encryption and decryption process, used to handle a big quantitiy of data (large messages) provided by the Python code implementing the RSA algorithm
    # Check if keys have already been generated
    if 'public_key' not in globals() or 'private_key' not in globals():
        # If keys have not been generated, generate a new key pair
        public_key, private_key = generate_keys(user_response_key_size // 4)
    else:
        # If keys already exist, retrieve the existing keys
        pass

    # Measure key generation complexity only if keys are generated
    if 'public_key' in globals() and 'private_key' in globals():
        # Measure the key generation complexity
        key_gen_time, key_gen_memory = measure_key_generation(user_response_key_size)

        # Ensure non-zero values for key generation complexity
        key_gen_time_str = "{:.8f}".format(max(0.00000001, key_gen_time))
        key_gen_memory_str = "{:.8f}".format(max(0.00000001, key_gen_memory))

        print("\nComplexity of key generation:")
        print("Time taken:", key_gen_time_str, "seconds")
        print("Memory used:", key_gen_memory_str, "KB")

    # Generate a plaintext message
    plaintext_message = "The challenges facing humanity today are numerous and complex. From climate change to global poverty, to social inequalities and the rise of terrorism, our world is confronted with urgent problems that require immediate and concerted action. To overcome these challenges, it is essential that we work together, as a global population, to find sustainable solutions. This requires a firm commitment to international cooperation, as well as concrete policies and actions to promote sustainable development, equality, and peace. By joining forces and pooling our resources, humanity can create a better future for all, where each individual has the opportunity to realize their full potential and live in a safe, just, and prosperous world. However, for the nations of the world to become rich and prosperous, global poverty must be eradicated for real."
    
    # Use plain text message to generate test messages
    test_messages = generate_test_messages(plaintext_message, 5)

    # Measure memory usage for generating test messages
    memory_used = measure_memory_usage()
    print("\nMemory used for generating test messages:", "{:.8f}".format(memory_used), "KB")

    # Measure encryption complexity for each test message
    print("\nMeasuring encryption complexity for each test message...")
    encryption_times = []  # Store encryption times for each message
    encrypted_messages = []  # Store encrypted messages for each message
    encoding_memory_used = []  # Store memory usage during encoding for each message
    encryption_memory_used_list = []  # Store memory usage during encryption for each message

    for i, message in enumerate(test_messages):
        # Encode the message
        encoded_message = encode_message(message)
    
        # Measure memory usage during encoding
        encoding_memory_used_value = measure_memory_usage()
        encoding_memory_used.append(encoding_memory_used_value)

        # Encrypt the message
        encryption_start_time = time.time()
        encrypted_message = [encrypt(char, public_key) for char in encoded_message]
        encryption_end_time = time.time()
        encryption_time = encryption_end_time - encryption_start_time
        encryption_times.append(encryption_time)
        encrypted_messages.append(encrypted_message)

        # Measure memory usage during encryption
        encryption_memory_used_value = measure_memory_usage()
        encryption_memory_used_list.append(encryption_memory_used_value)

        # Display information
        print(f"Message {i+1}:")
        print("Clear message:", message)
        print("Encrypted message:", encrypted_message)
        print(f"Encryption time for message {i+1}: {encryption_time:.8f} seconds")
        print("Memory used during encoding:", "{:.8f}".format(encoding_memory_used_value), "KB")
        print("Memory used during encryption:", "{:.8f}".format(encryption_memory_used_value), "KB")

    # Calculate average encryption time
    average_encryption_time = sum(encryption_times) / len(encryption_times)
    print("\nAverage encryption time:", "{:.8f}".format(average_encryption_time), "seconds")

    # Calculate average encoding time
    average_encoding_time = sum(encryption_times) / len(encryption_times)
    print("Average encoding time:", "{:.8f}".format(average_encoding_time), "seconds")

    # Calculate average memory used during encryption
    average_encryption_memory = sum(encryption_memory_used_list) / len(encryption_memory_used_list)
    print("Average memory used during encryption:", "{:.8f}".format(average_encryption_memory), "KB")

    # Calculate average memory used during encoding
    average_encoding_memory = sum(encoding_memory_used) / len(encoding_memory_used)
    print("Average memory used during encoding:", "{:.8f}".format(average_encoding_memory), "KB")

    # Measure decryption complexity for each test message
    print("\nMeasuring decryption complexity for each test message...")
    decryption_times = []  # Store decryption times for each message
    decrypted_messages = []  # Store decrypted messages for each message
    decoding_memory_used = []  # Store memory usage during decoding for each message
    decryption_memory_used_list = []  # Store memory usage during decryption for each message

    for i, encrypted_message in enumerate(encrypted_messages):
        # Decrypt the message
        decryption_start_time = time.time()
        decrypted_message = [decrypt(char, private_key) for char in encrypted_message]
        decryption_end_time = time.time()
        decryption_time = decryption_end_time - decryption_start_time
        decryption_times.append(decryption_time)
        decrypted_messages.append(decrypted_message)

        # Measure memory usage during decryption
        decryption_memory_used_value = measure_memory_usage()
        decryption_memory_used_list.append(decryption_memory_used_value)

        # Measure memory usage during decoding
        decoding_memory_used_value = measure_memory_usage()
        decoding_memory_used.append(decoding_memory_used_value)

        # Display information
        print(f"Message {i+1}:")
        print("Encrypted message:", encrypted_message)
        decrypted_message_text = ''.join([chr(char) if char < 1114111 else '?' for char in decrypted_message])
        print("Decrypted message:", decrypted_message_text)
        print(f"Decryption time for message {i+1}: {decryption_time:.8f} seconds")
        print("Memory used during decryption:", "{:.8f}".format(decryption_memory_used_value), "KB")
        print("Memory used during decoding:", "{:.8f}".format(decoding_memory_used_value), "KB")

    # Calculate average decryption time
    average_decryption_time = sum(decryption_times) / len(decryption_times)
    print("\nAverage decryption time:", "{:.8f}".format(average_decryption_time), "seconds")

    # Calculate average decoding time
    average_decoding_time = sum(decryption_times) / len(decryption_times)
    print("Average decoding time:", "{:.8f}".format(average_decoding_time), "seconds")

    # Calculate average memory used during decryption
    average_decryption_memory = sum(decryption_memory_used_list) / len(decryption_memory_used_list)
    print("Average memory used during decryption:", "{:.8f}".format(average_decryption_memory), "KB")

    # Calculate average memory used during decoding
    average_decoding_memory = sum(decoding_memory_used) / len(decoding_memory_used)
    print("Average memory used during decoding:", "{:.8f}".format(average_decoding_memory), "KB")

    # Generate test message for encoding and decoding
    test_message = generate_message(user_response_message_length)

    # Measure encoding complexity
    print("\nMeasuring encoding complexity...")
    encoding_start_time = time.time()
    encoded_message = encode_message(test_message)
    encoding_end_time = time.time()
    encoding_time = encoding_end_time - encoding_start_time
    encoding_memory_used = measure_memory_usage() # Measure memory usage during encoding
    print("Encoding time:", "{:.8f}".format(encoding_time), "seconds")
    print("Memory used during encoding:", "{:.8f}".format(encoding_memory_used), "KB")

    # Measure decoding complexity
    print("\nMeasuring decoding complexity...")
    decoding_start_time = time.time()
    decoded_message = decode_message(encoded_message)
    decoding_end_time = time.time()
    decoding_time = decoding_end_time - decoding_start_time
    decoding_memory_used = measure_memory_usage() # Measure memory usage during decoding
    print("Decoding time:", "{:.8f}".format(decoding_time), "seconds")
    print("Memory used during decoding:", "{:.8f}".format(decoding_memory_used), "KB")

    # Measure encryption complexity
    print("\nMeasuring encryption complexity...")
    encryption_start_time = time.time()
    encrypted_message = [encrypt(char, public_key) for char in encoded_message]
    encryption_end_time = time.time()
    encryption_time = encryption_end_time - encryption_start_time
    encryption_memory_used = measure_memory_usage() # Measure memory usage during encryption
    print("Encryption time:", "{:.8f}".format(encryption_time), "seconds")
    print("Memory used during encryption:", "{:.8f}".format(encryption_memory_used), "KB")
    
    # Measure decryption complexity
    print("\nMeasuring decryption complexity...")
    decryption_start_time = time.time()
    decrypted_message = [decrypt(char, private_key) for char in encrypted_message]
    decryption_end_time = time.time()
    decryption_time = decryption_end_time - decryption_start_time
    decryption_memory_used = measure_memory_usage() # Measure memory usage during decryption
    print("Decryption time:", "{:.8f}".format(decryption_time), "seconds")
    print("Memory used during decryption:", "{:.8f}".format(decryption_memory_used), "KB")
