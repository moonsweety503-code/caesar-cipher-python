alphabet = 'abcdefghijklmnopqrstuvwxyz'

def caesar(text, shift, direction):
    result = ""

    # Normalize shift (handles large numbers)
    shift = shift % 26

    if direction == "decode":
        shift = -shift

    for char in text:
        if char in alphabet:
            new_position = (alphabet.index(char) + shift) % 26
            result += alphabet[new_position]
        else:
            result += char  # keeps spaces, numbers, symbols

    return result


# Program loop
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    output = caesar(text, shift, direction)

    if direction == "encode":
        print(f"Encoded result: {output}")
    else:
        print(f"Decoded result: {output}")

    restart = input("Type 'yes' to continue or 'no' to exit:\n").lower()
    if restart == "no":
        print("Goodbye 👋")
        break
