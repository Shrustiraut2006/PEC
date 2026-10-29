
import subprocess

gpg = r"C:\Program Files\GnuPG\bin\gpg.exe"

print("\n1. Generate key pair")
print("2. List public keys")
print("3. List secret keys")
print("4. Encrypt a message")
print("5. Decrypt a message")

choice = input("Enter choice: ")

if choice == "1":
    subprocess.run([gpg, "--full-generate-key"])

elif choice == "2":
    subprocess.run([gpg, "--list-keys"])

elif choice == "3":
    subprocess.run([gpg, "--list-secret-keys"])

elif choice == "4":
    message = input("Enter message: ")

    with open("message.txt", "w") as file:
        file.write(message)

    result = subprocess.run([
        gpg, "--yes", "--output", "message.txt.gpg",
        "--encrypt", "--recipient",
        "shrustiraut2006@gmail.com", "message.txt"
    ])

    if result.returncode == 0:
        print("Encryption successful!")
    else:
        print("Encryption failed. Check the GPG error above.")

elif choice == "5":
    result = subprocess.run([
        gpg, "--output", "decrypted.txt",
        "--decrypt", "message.txt.gpg"
    ])

    if result.returncode == 0:
        print("Decryption successful!")
        with open("decrypted.txt", "r") as file:
            print("Decrypted message:", file.read())
    else:
        print("Decryption failed. Check the GPG error above.")

else:
    print("Invalid choice.")

