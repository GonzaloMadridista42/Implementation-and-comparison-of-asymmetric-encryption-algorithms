from nacl.public import PrivateKey
import binascii

privKey = PrivateKey.generate()
pubKey = privKey.public_key

print("privKey:", binascii.hexlify(bytes(privKey)))
print("pubKey: ", binascii.hexlify(bytes(pubKey)))