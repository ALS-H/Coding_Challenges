#: Write a program to multiply two matrices 

def mul_mats(mat1, mat2):
    m1 = len(mat1)
    n1 = len(mat1[0]) if mat1 else 0
    
    m2 = len(mat2)
    n2 = len(mat2[0]) if mat2 else 0

    if n1 != m2:
        raise ValueError("Matrix dimensions do not match for multiplication")
    
    # Initialize result matrix with zeros
    res_mat = [[0]*n2 for _ in range(m1)]
    
    for i in range(m1):
        for j in range(n2):
            for k in range(n1):
                res_mat[i][j] += mat1[i][k] * mat2[k][j]
                
    return res_mat

#test cases
# 2x3 multiplied by 3x2
assert mul_mats([[1,2,3],[4,5,6]], [[7,8],[9,10],[11,12]]) == [[58,64],[139,154]]

#neg: dimension mismatch
try:
    mul_mats([[1,2]], [[1,2]])  # 1x2 * 1x2 wrong
except ValueError:
    pass

#edge
# Empty matrices
assert mul_mats([], []) == []
# Matrix with one row or one column
assert mul_mats([[1,2,3]], [[4],[5],[6]]) == [[32]]  # 1x3 * 3x1 -> 1x1
# Multiplying with 1xN or Nx1 matrices
assert mul_mats([[1],[2],[3]], [[4,5,6]]) == [[4,5,6],[8,10,12],[12,15,18]]  # 3x1 * 1x3 -> 3x3

print("All test cases passed!")

if __name__ == "__main__":
    print("Matrix 1:")
    r1 = int(input("Enter number of rows: "))
    c1 = int(input("Enter number of columns: "))
    mat1 = []
    for i in range(r1):
        row = list(map(int, input(f"Enter row {i+1} elements: ").split()))
        if len(row) != c1:
            raise ValueError("Row length mismatch")
        mat1.append(row)
    
    print("\nMatrix 2:")
    r2 = int(input("Enter number of rows: "))
    c2 = int(input("Enter number of columns: "))
    mat2 = []
    for i in range(r2):
        row = list(map(int, input(f"Enter row {i+1} elements: ").split()))
        if len(row) != c2:
            raise ValueError("Row length mismatch")
        mat2.append(row)
    
    result = mul_mats(mat1, mat2)
    print("\nResultant Matrix:")
    for row in result:
        print(*row)

