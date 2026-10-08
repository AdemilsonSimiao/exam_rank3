def whisper_cipher(text: str, shift: int) -> str:
    ...

def main():
    print(whisper_cipher("el", -3))

if __name__ == "__main__":
    main()

# Write a function that creates a Caesar cipher by shifting letters in a
# string by a given amount.
# Non-alphabetic characters should remain unchanged.
# The shift can be negative (shift left).