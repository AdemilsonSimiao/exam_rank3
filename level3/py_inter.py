def inter(s1: str, s2: str) -> str:
    string = ""
    for c in s1:
        if c in s2 and c not in string:
            string += c
    return string

def main():
    print(inter("aaaabbbb", "bac"))

if __name__ == "__main__":
    main()
# Write a function that returns a string with the characters that appear
# in both strings, without repetitions. Characters are added in the order
# they appear in the first string.