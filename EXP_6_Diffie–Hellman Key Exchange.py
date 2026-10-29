p = int(input("Enter prime number p: "))
g = int(input("Enter generator g: "))
a = int(input("Enter Alice's private key: "))
b = int(input("Enter Bob's private key: "))

if p <= 2 or not 1 < g < p or a <= 0 or b <= 0:
    print("Enter valid values.")
else:
    A = pow(g, a, p)
    B = pow(g, b, p)

    secret1 = pow(B, a, p)
    secret2 = pow(A, b, p)

    print("Alice public key:", A)
    print("Bob public key:", B)
    print("Alice shared secret:", secret1)
    print("Bob shared secret:", secret2)
    print("Keys match:", secret1 == secret2)