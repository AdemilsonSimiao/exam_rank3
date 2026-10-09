def string_sculptor(text: str) -> str:
    string = ""
    i = 0
    for c in text:
        if c == " ":
            i = 0
            string += c
        elif c.isalpha():
            string += c.lower() if i % 2 == 0 else c.upper()
            i += 1
        else:
            string += c
    return string

def main():
    print(string_sculptor("a bc"))

if __name__ == "__main__":
    main()

# Write a function that transforms a string by alternating the case of
# alphabetic characters only.
# Non-alphabetic characters remain unchanged and are NOT counted in the
# alternation index.
# The first alphabetic character should be lowercase, the second uppercase, etc.
# Spaces reset the alternation (next alpha after a space is lowercase again).
