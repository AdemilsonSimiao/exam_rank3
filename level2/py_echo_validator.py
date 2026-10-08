def echo_validator(text: str) -> bool:
    clean = [c.lower() for c in text if c.isalpha()]
    return clean == clean[::-1] if clean else False

def main():
    print(echo_validator("a"))
    
if __name__ == "__main__":
    main()

# Write a function that checks if a string is a palindrome,
# ignoring spaces and case, only considering alphabetic characters
# for the comparison.
# Steps to implemetantion:
# check if not text == empty (if empty, return False)
# create an empty variable
# loop through the text to check if each character is alphabetic
# concatenete into variable
# keep the alphabetic characters in a variable in a lowercase
# create variables to start until end of the text, comparing in a loop
# check if start is different of the end. If different return False
# finally, return True

