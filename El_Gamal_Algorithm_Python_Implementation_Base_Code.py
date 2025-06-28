import random
from math import pow

def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)

def gen_key(q):
    key = random.randint(int(pow(10, 20)), int(q))
    while gcd(q, key) != 1:
        key = random.randint(int(pow(10, 20)), int(q))
    return key

def power(a, b, c):
    x = 1
    y = a
    while b > 0:
        if b % 2 == 0:
            x = (x * y) % c
        y = (y * y) % c
        b = int(b / 2)
    return x % c

def encryption(msg, q, h, g):
    ct = []
    k = gen_key(q)
    s = power(h, k, q)
    p = power(g, k, q)
    print("g^k used:", p)
    print("g^ak used:", s)
    print("Original Message:", msg)
    for i in range(0, len(msg)):
        ct.append(s * ord(msg[i]))
    print("Encrypted Message:", ct)
    return ct, p

def decryption(ct, p, key, q):
    pt = []
    h = power(p, key, q)
    for i in range(0, len(ct)):
        pt.append(chr(int(ct[i] / h)))
    return pt

def main():
    msg = input("Enter message: ")
    q = random.randint(int(pow(10, 20)), int(pow(10, 50)))  # Utilisation de pow() pour générer q
    g = random.randint(2, q)
    key = gen_key(q)
    h = power(g, key, q)
    print("g used:", g)
    print("g^a used:", h)
    ct, p = encryption(msg, q, h, g)
    print("Original Message:", msg)
    print("Encrypted Message:", ct)
    pt = decryption(ct, p, key, q)
    d_msg = ''.join(pt)
    print("Decrypted Message:", d_msg)

if __name__ == "__main__":
    main()