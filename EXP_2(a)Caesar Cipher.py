def caesar(text, shift):
    result = ""

    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - 65 + shift) % 26 + 65)
        elif ch.islower():
            result += chr((ord(ch) - 97 + shift) % 26 + 97)
        else:
            result += ch

    return result


message = input("Enter message: ")
shift = int(input("Enter shift value: "))

encrypted = caesar(message, shift)

print("Encrypted message:", encrypted)
print("Decrypted message:", caesar(encrypted, -shift))