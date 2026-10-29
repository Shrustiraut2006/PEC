import math

p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if not is_prime(p) or not is_prime(q) or p == q:
    print("Enter two different prime numbers.")
else:
    n = p * q
    phi = (p - 1) * (q - 1)

    e = next(
        (x for x in range(2, phi) if math.gcd(x, phi) == 1),
        None
    )

    if e is None:
        print("Choose larger prime numbers.")
    else:
        d = pow(e, -1, phi)
        message = int(input(f"Enter message number (0 to {n-1}): "))

        if 0 <= message < n:
            cipher = pow(message, e, n)
            plain = pow(cipher, d, n)

            print("Public key:", (e, n))
            print("Private key:", (d, n))
            print("Encrypted message:", cipher)
            print("Decrypted message:", plain)
        else:
            print("Message must be between 0 and n-1.")