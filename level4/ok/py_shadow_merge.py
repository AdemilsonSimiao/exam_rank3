def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    return sorted(list1 + list2)

def main():
    print(shadow_merge([1,3,5], [2,4,6]))

if __name__ == "__main__":
    main()

# Write a function that merges two sorted lists into one sorted list.