def whisper_cipher(text: str, shift: int) -> str:
    res = ""
    for c in text:
        if "a" <= c <= "z":
            base = ord("a")
        elif "A" <= c <= "Z":
            base = ord("A")
        else:
            res += c
            continue
        res += chr((ord(c) - base + shift) % 26 + base)
    return res

def main():
    print(whisper_cipher("a", -3))

if __name__ == "__main__":
    main()

# Write a function that creates a Caesar cipher by shifting letters in a
# string by a given amount.
# Non-alphabetic characters should remain unchanged.
# The shift can be negative (shift left).