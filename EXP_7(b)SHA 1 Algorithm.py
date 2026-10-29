import hashlib

message = input("Enter message: ")
result = hashlib.sha1(message.encode()).hexdigest()

print("SHA-1 hash:", result)