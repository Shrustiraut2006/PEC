import math

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

gcd = math.gcd(a, b)
lcm = abs(a * b) // gcd if gcd != 0 else 0

print("GCD =", gcd)
print("LCM =", lcm)