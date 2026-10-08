def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    if not (2 <=  from_base <= 36 and 2 <= to_base <= 36):
        return "ERROR"
    try:
        decimal = int(number, from_base)
    except ValueError:
        return "ERROR"
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while decimal > 0 or not result:
        result = digits[decimal % to_base] + result
        decimal //= to_base
    return result

def main():
    print(number_base_converter("1010", 2, 10))

if __name__ == "__main__":
    main()

# Write a function that converts a number from one base to another.
# Support bases from 2 to 36 inclusive.
# Use digits 0-9 and letters A-Z for values 10-35.
# Return "ERROR" for invalid inputs.