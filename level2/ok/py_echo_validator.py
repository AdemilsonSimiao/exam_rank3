def echo_validator(text: str) -> bool:
    clean = [c.lower() for c in text if c.isalpha()]
    return clean == clean[::-1] if clean else False

def main():
    print(echo_validator("an,: a"))

if __name__ == "__main__":
    main()

# Write a function that checks if a string is a palindrome,
# ignoring spaces and case, only consider alphabetic characters
# for the comparison.