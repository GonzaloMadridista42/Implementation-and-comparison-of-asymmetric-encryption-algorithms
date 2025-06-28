hex_value = "4c750ba67b03d54f5a51bfab76aaab402a01c7950dee72dc44048822b73b2baf"
binary_value = bin(int(hex_value, 16))[2:]  # Convertit le hex en binaire, puis supprime le préfixe '0b'
print("Nombre binaire colossal :", binary_value)