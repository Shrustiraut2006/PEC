def encrypt(message, rails):
    rows = [""] * rails
    row = 0
    direction = 1

    for ch in message:
        rows[row] += ch

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    return "".join(rows)


message = input("Enter message: ")
rails = int(input("Enter number of rails: "))

if rails < 2:
    print("Enter at least 2 rails.")
else:
    print("Encrypted message:", encrypt(message, rails))