message = input("Enter message: ").replace(" ", "")
columns = int(input("Enter number of columns: "))

if columns <= 0:
    print("Columns must be positive.")
else:
    while len(message) % columns != 0:
        message += "X"

    rows = [
        message[i:i+columns]
        for i in range(0, len(message), columns)
    ]

    print("Message Rectangle:")
    for row in rows:
        print(" ".join(row))

    order = input("Enter column order (e.g. 3 1 2): ").split()
    order = [int(x) for x in order]

    if sorted(order) != list(range(1, columns+1)):
        print("Invalid column order.")
    else:
        cipher = ""
        for col in order:
            for row in rows:
                cipher += row[col-1]

        print("Encrypted message:", cipher)