def encrypt(raw, n, m):
    encrypted = ''
    for c in raw:
        if 'a' <= c <= 'z':  # Lowercase letters
            encrypted += chr((ord(c) - ord('a') + (n * m)) % 26 + ord('a'))
        elif 'A' <= c <= 'Z':  # Uppercase letters
            encrypted += chr((ord(c) - ord('A') + (n * m)) % 26 + ord('A'))
        else:  # Non-alphabetic characters
            encrypted += c
    return encrypted

def decrypt(encrypted, n, m):
    decrypted = ''
    for c in encrypted:
        if 'a' <= c <= 'z':  # Lowercase letters
            decrypted += chr((ord(c) - ord('a') - (n * m)) % 26 + ord('a'))
        elif 'A' <= c <= 'Z':  # Uppercase letters
            decrypted += chr((ord(c) - ord('A') - (n * m)) % 26 + ord('A'))
        else:  # Non-alphabetic characters
            decrypted += c
    return decrypted

def verify(raw, decrypted):
    return raw == decrypted

# User inputs for n and m
n, m = 2, 5  # Example values

# Read raw text
with open('raw_text.txt', encoding='utf-8') as f:
    raw_text = f.read()

# Encrypt the text
encrypted_text = encrypt(raw_text, n, m)
with open('encrypted_text.txt', 'w', encoding='utf-8') as f:
    f.write(encrypted_text)

# Decrypt the text
decrypted_text = decrypt(encrypted_text, n, m)



# Verify correctness
is_correct = verify(raw_text, decrypted_text)
print("Decryption Correct:", is_correct)

print("Decrypted Text:")
print(decrypted_text)
