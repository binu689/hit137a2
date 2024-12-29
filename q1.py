def encrypt(raw, n, m):
    encrypted = ''
    for c in raw:
        if c >= 'a' and c <= 'm':
            encrypted += chr((ord(c) - ord('a') + (n * m)) % 13 + ord('a'))
        elif c >= 'n' and c <= 'z':
            encrypted += chr((ord(c) - ord('n') - (n + m)) % 13 + ord('n'))
        elif c >= 'A' and c <= 'M':
            encrypted += chr((ord(c) - ord('A') - (n)) % 13 + ord('A'))
        elif c >= 'N' and c <= 'Z':
            encrypted += chr((ord(c) - ord('N') + (m ** 2)) % 13 + ord('N'))
        else:  # Non-alphabetic characters
            encrypted += c
    return encrypted


def decrypt(encrypted, n, m):
    decrypted = ''
    for c in encrypted:
        if c >= 'a' and c <= 'm':
            decrypted += chr((ord(c) - ord('a') - (n * m)) % 13 + ord('a'))            
        elif c >= 'n' and c <= 'z':
            decrypted += chr((ord(c) - ord('n') + (n + m)) % 13 + ord('n'))            
        elif c >= 'A' and c <= 'M':
            decrypted += chr((ord(c) - ord('A') + (n)) % 13 + ord('A'))            
        elif c >= 'N' and c <= 'Z':
            decrypted += chr((ord(c) - ord('N') - (m ** 2)) % 13 + ord('N'))            
        else:  # Non-alphabetic characters
            decrypted += c
    return decrypted


def verify(raw, decrypted):
    return raw == decrypted


# User inputs for n and m
n = int(input('Enter integer n: '))
m = int(input('Enter integer m: '))

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
