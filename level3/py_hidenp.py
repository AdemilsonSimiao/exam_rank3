def hidenp(small: str, big: str) -> bool:
    biig = iter(big)
    return all(c in biig for c in small)

def main():
    print(hidenp("a", "abc"))

if __name__ == "__main__":
    main()

# Write a function that checks if the string 'small' is a subsequence
# of 'big'. A subsequence means all characters of 'small' appear in 'big'
# in the same order, but not necessarily consecutively.
# Function is case-sensitive.