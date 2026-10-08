def string_permutation_checker(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)

def main():
    print(string_permutation_checker("abc", "bca"))

if __name__ == "__main__":
    main()

# Write a function that determines if two strings are permutations of each other.
# Case sensitive. Whitespace and punctuation count as regular characters.
# Empty strings are permutations of each other.