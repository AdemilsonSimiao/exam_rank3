def anagram(s1: str, s2: str) -> bool:
    c1 = sorted(s1.lower().replace(" ", ""))
    c2 = sorted(s2.lower().replace(" ", ""))
    return c1 == c2

def main():
    print(anagram("ana", "ana"))

if __name__ == "__main__":
    main()

# Write a function that checks if two strings are anagrams.
# They must contain exactly the same letters with the same quantity,
# ignoring case and spaces.