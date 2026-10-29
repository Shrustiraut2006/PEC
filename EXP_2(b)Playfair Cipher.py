def create_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    letters = ""

    for ch in (key.upper() + alphabet):
        if ch.isalpha():
            ch = "I" if ch == "J" else ch
            if ch not in letters:
                letters += ch

    return [list(letters[i:i+5]) for i in range(0, 25, 5)]


def encrypt(message, matrix):
    text = "".join(c for c in message.upper() if c.isalpha())
    text = text.replace("J", "I")
    pairs = []
    i = 0

    while i < len(text):
        a = text[i]

        if i + 1 == len(text):
            b = "X"
            i += 1
        elif text[i] == text[i+1]:
            b = "X"
            i += 1
        else:
            b = text[i+1]
            i += 2

        pairs.append((a, b))

    result = ""

    for a, b in pairs:
        for r in range(5):
            for c in range(5):
                if matrix[r][c] == a:
                    r1, c1 = r, c
                if matrix[r][c] == b:
                    r2, c2 = r, c

        if r1 == r2:
            result += matrix[r1][(c1+1) % 5]
            result += matrix[r2][(c2+1) % 5]
        elif c1 == c2:
            result += matrix[(r1+1) % 5][c1]
            result += matrix[(r2+1) % 5][c2]
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result


key = input("Enter keyword: ")
message = input("Enter message: ")

matrix = create_matrix(key)

print("Key Matrix:")
for row in matrix:
    print(" ".join(row))

print("Encrypted message:", encrypt(message, matrix))