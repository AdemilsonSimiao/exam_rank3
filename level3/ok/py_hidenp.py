def hidenp(small: str, big: str) -> bool:
    lengh = len(small)
    cont = 0
    i = 0
    j = 0
    while i < lengh:
        while j < len(big):
            if small[i] == big[j]:
                cont += 1
                j += 1
                break
            j += 1
        i += 1
    return lengh == cont

def main():
    print(hidenp("oi", "Olai"))
    
if __name__ == "__main__":
    main()

# Write a function that checks if the string 'small' is a subsequence
# of 'big'. A subsequence means all characters of 'small' appear in 'big'
# in the same order, but not necessarily consecutively.
# Function is case-sensitive.