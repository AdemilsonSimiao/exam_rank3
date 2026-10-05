def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    new_matrix = []
    for row in matrix:
        new_row = []
        for i in range(len(row) - 1, -1, -1):
            new_row.append(row[i])
        new_matrix.append(new_row)
    return new_matrix

# def main():
#     print(mirror_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))

# if __name__ == "__main__":
#     main()

# Given a 2D matrix (list of lists), return a new matrix where each row
# is reversed.