def whisper_cipher(text: str, shift: int) -> str:
    cipher = ""
    for c in text:
        if "a" <= c <= "z":
            amount = ord("a")
        elif "A" <= c <= "Z":
            amount = ord("A")
        else:
            cipher += c
            continue
        cipher += chr((ord(c) - amount + shift) % 26 + amount)
    return cipher

def main():
    print(whisper_cipher("el", -3))

if __name__ == "__main__":
    main()

# Write a function that creates a Caesar cipher by shifting letters in a
# string by a given amount.
# Non-alphabetic characters should remain unchanged.
# The shift can be negative (shift left).