"""  Write a program to store elements into a M * N matrix of 
integer. Display the matrix and its transpose
"""

def store_td_arr(m, n):
    matrix = [[0]*n for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            while True:
                try:
                    matrix[i][j] = int(input(f"Enter element [{i+1},{j+1}]: "))
                    break
                except ValueError:
                    print("Please enter an integer.")
    
    return matrix

def display(mat):
    for row in mat:
        print(*row)

def transpose(mat):
    if not mat or not mat[0]:
        return []
    m = len(mat)
    n = len(mat[0])
    
    mat2 = []
    for j in range(n):
        row = []
        for i in range(m):
            row.append(mat[i][j])
        mat2.append(row)
        
    return mat2

#test cases
assert transpose([[1,2],[3,4],[5,6]]) == [[1,3,5],[2,4,6]]
# Single row matrix
assert transpose([[1,2,3]]) == [[1],[2],[3]]
# Single column matrix
assert transpose([[1],[2],[3]]) == [[1,2,3]]
assert transpose([[1,-2],[3,-4]]) == [[1,3],[-2,-4]]
#edge cases
assert transpose([]) == []
assert transpose([[5]]) == [[5]]

print("All test cases passed!")

if __name__ == "__main__":
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))

    print("\nEnter the elements of the matrix:")
    mat = store_td_arr(m, n)

    print("\nOriginal Matrix:")
    display(mat)

    mat_t = transpose(mat)
    print("\nTranspose of the Matrix:")
    display(mat_t)
