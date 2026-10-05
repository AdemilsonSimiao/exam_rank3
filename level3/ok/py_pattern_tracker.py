def pattern_tracker(text: str) -> int:
    count = 0
    for i in range(len(text) - 1):
        char1 = text[i]
        char2 = text[i+1]
        if char1.isdigit() and char2.isdigit():
            num1 = int(char1)
            num2 = int(char2)
            if num2 == num1 + 1:
                count += 1
    return count

def main():
    print(pattern_tracker("12a34"))

if __name__ == "__main__":
    main()

# Write a function that counts the number of valid consecutive digit pairs
# in a string. A valid pair consists of two adjacent digits where the second
# digit is exactly one greater than the first.
# A 9 followed by a 0 is NOT a valid pair.