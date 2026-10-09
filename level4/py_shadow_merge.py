def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    return sorted(list1) + sorted(list2)

def main():
    print(shadow_merge([1,2,3], [4,5,6]))

if __name__ == "__main__":
    main()

# Write a function that merges two sorted lists into one sorted list.
