
import os
import subprocess

gpg = r"C:\Program Files\GnuPG\bin\gpg.exe"

print("\n1. Encrypt a file")
print("2. Decrypt a file")
print("3. Digitally sign a file")
print("4. Verify a signature")

choice = input("Enter choice: ")

if choice == "1":
    filename = input("Enter file path: ").strip('"')
    recipient = input("Enter recipient email or key ID: ")

    if not os.path.isfile(filename):
        print("File not found.")
    else:
        output = filename + ".asc"
        result = subprocess.run([
            gpg, "--armor", "--output", output,
            "--encrypt", "--recipient", recipient, filename
        ])
        if result.returncode == 0:
            print("Encrypted file:", output)
        else:
            print("Encryption failed.")

elif choice == "2":
    filename = input("Enter encrypted file path: ").strip('"')
    if os.path.isfile(filename):
        subprocess.run([gpg, "--output", "decrypted.txt",
                        "--decrypt", filename])
    else:
        print("File not found.")

elif choice == "3":
    filename = input("Enter file path to sign: ").strip('"')
    if os.path.isfile(filename):
        result = subprocess.run([
            gpg, "--armor", "--clearsign", filename
        ])
        if result.returncode == 0:
            print("Digital signature created:", filename + ".asc")
        else:
            print("Signing failed.")
    else:
        print("File not found.")

elif choice == "4":
    filename = input("Enter signed file path: ").strip('"')

    if os.path.isfile(filename):
        subprocess.run([gpg, "--verify", filename])
    else:
        print("File not found.")

else:
    print("Invalid choice.")
