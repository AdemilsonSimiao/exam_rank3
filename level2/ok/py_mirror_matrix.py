def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    
    return [row[::-1] for row in matrix]

# def main():
#     print(mirror_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))

# if __name__ == "__main__":
#     main()

# Given a 2D matrix (list of lists), return a new matrix where each row
# is reversed.