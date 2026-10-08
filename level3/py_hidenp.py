def hidenp(small: str, big: str) -> bool:
    it = iter(big)
    return all( c in it for c in small)

def main():
    print(hidenp("", "abc"))

if __name__ == "__main__":
    main()

# Write a function that checks if the string 'small' is a subsequence
# of 'big'. A subsequence means all characters of 'small' appear in 'big'
# in the same order, but not necessarily consecutively.
# Function is case-sensitive.