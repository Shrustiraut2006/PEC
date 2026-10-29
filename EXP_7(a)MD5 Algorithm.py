import hashlib

message = input("Enter message: ")

digest = hashlib.md5(message.encode()).hexdigest()

print("MD5 Hash:", digest)