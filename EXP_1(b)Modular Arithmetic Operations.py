import math

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
m = int(input("Enter modulus: "))

if m <= 0:
    print("Modulus must be positive.")
else:
    print("Addition =", (a + b) % m)
    print("Subtraction =", (a - b) % m)
    print("Multiplication =", (a * b) % m)

    if math.gcd(b, m) == 1:
        print("Division =", (a * pow(b, -1, m)) % m)
    else:
        print("Division not possible")