def bracket_validator(s: str) -> bool:
    stack = []
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{',
    }
    for c in s:
        if c in "([{":
            stack.append(c)
        if c in ")]}":
            if not stack:
                return False
            if stack[-1] != pairs[c]:
                return False
            stack.pop()
    return not stack

    
#  Write a function that chackes if the brackets in a string are valid.
#  A string os valid if every opening bracket has a matching closing bracket int the correct order.
#  Allowed brackets: (), [], {}
#  Logic
#  for each character in the string
#  if it's an opening bracket, push it onto the stack.
#  if it's a closing bracket, check the top of the stack.
#  if the stack is empty, the string is invalid
#  if the top of the stack doesn't match the corresponding opening bracket, retuen false.
#  the corresponding opening bracket
#  if it matches, pop it from the stack.
#  if it doesn't match, the string is invalid
#  At the end, the stack must be empty
