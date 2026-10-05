def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    ...
 
def main():
    print(mirror_matrix([[1,2,3],[4,5,6]]))


if __name__ == "__main__":
    main()

# Given a 2D matrix (list of lists), return a new matrix where each row
# is reversed.
# Steps to implementation
# Create a empty new martrix variable
# loop through matrix looking row by row
# Create a new row to keep a reversed row
# loop through row looking number from matrix list
# keep a reversed row in a new_row using append function
# keep a reversed matrix in a new_matrix using append function
# Finaly, return a new matrix variable