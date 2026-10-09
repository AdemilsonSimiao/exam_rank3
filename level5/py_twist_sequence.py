def twist_sequence(arr: list[int], k: int) -> list[int]:
    if not arr:
       return arr
    return arr[-k:] + arr[:-k]

def main():
    print(twist_sequence([1, 2, 3], 2))

if __name__ == "__main__":
    main()

# Write a function that rotates an array to the right by k positions.
# Rotating right by k means the last k elements move to the front.