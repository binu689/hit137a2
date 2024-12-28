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
        else:
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
        else:
            decrypted += c
    return decrypted


n, m = 2, 5  # test values

with open('raw_text.txt') as f:
    raw_text = f.read()

encrypted_text = encrypt(raw_text, n, m)
with open('encrypted_text.txt', 'w') as f:
    f.write(encrypted_text)
