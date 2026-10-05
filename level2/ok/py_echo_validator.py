def echo_validator(text: str) -> bool:
    if not text:
        return False
    clean: str = ""
    for c in text:
        if c.isalpha():
            clean += c
    clean = clean.lower()
    start = 0
    end = len(clean) -1
    while  start < end:
        if clean[start] != clean[end]:
            return False
        start += 1
        end -= 1
    return True

# def main():
#     print(echo_validator("an,: a"))

# if __name__ == "__main__":
#     main()

# Write a function that checks if a string is a palindrome,
# ignoring spaces and case, only consider alphabetic characters
# for the comparison.