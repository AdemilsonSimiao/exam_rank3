def anagram(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)

def main():
    print(anagram("ana", "an"))

if __name__ == "__main__":
    main()

# Write a function that checks if two strings are anagrams.
# They must contain exactly the same letters with the same quantity,
# ignoring case and spaces.