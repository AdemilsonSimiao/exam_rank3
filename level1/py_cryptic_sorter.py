def cryptic_sorter(strings: list[str]) -> list[str]:
    def key(s):
        length = len(s)
        insensitively = s.lower()
        vowels = sum(
            c in "aeiou"
            for c in insensitively
        )
        return [length, insensitively, vowels]
    result = strings.copy()
    for i in range(len(result)):
        for j in range(len(result) -1 -i):
            if key(result[j]) > key(result[j + 1]):
                result[j], result[j + 1] = result[j + 1], result[j]
    return result

def main():
    print(cryptic_sorter(["hello","world","hi","test"]))

if __name__ == "__main__":
    main()

# Write a function that sorts a list of strings according to multiple criteria:
# 1. Primary sort: By string length (shortest first)
# 2. Secondary sort: ASCII order, except letters are compared case-insensitively
#    (for strings of same length)
# 3. Tertiary sort: By number of vowels (ascending, for same length and lexically equal)
# 4. Equal strings will appear in the same order as in the input list.
# Forbidden functions: sorted(), list.sort()