#Write a program to create a 2D array and display its elements row-wise

def twoD_arr(m,n):
    matrix=[[0]*n for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            matrix[i][j]=int(input("Enter a ele:"))
    
    return matrix

def display_row_wise(mat):
    for row in mat:
        print(*row)

if __name__=="__main__":
    m=int(input("Enter number of rows:"))
    n=int(input("Enter the number cols:"))
    
    mat=twoD_arr(m,n)
    
    display_row_wise(mat)
    
    