def bracket_validator(s: str) -> bool:
    stack = []
    brackets = {
       ")": "(",
       "]": "[",
       "}": "{",
    }
    for c in s:
        if c in "([{":
           stack.append(c)
        elif c in ")]}":
            if not stack:
                return False
            if stack[-1] != brackets[c]:
                return False
            stack.pop()
    return not stack
        

def main():
    print(bracket_validator("({})"))

if __name__ == "__main__":
    main()


# Write a function that checks if the brackets in a string are valid.
# A string is valid if every opening bracket has a matching closing bracket
# in the correct order.
# Allowed brackets: (), [], {}