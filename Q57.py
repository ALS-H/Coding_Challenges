#Write a program to check if a given element exists in a 2D array

def search_an_ele(mat,target):
    for row in mat:
        if target in row:
            return True
    return False

#test cases
#positive
assert search_an_ele([[1, 2], [3, 4]], 3) == True
#negative
assert search_an_ele([[0, -1], [5, 7]], 2) == False
#edge case
# Matrix with empty rows
assert search_an_ele([[], []], 0) == False

print("All test cases passed!")

if __name__ == "__main__":
    r = int(input("Enter number of rows: "))
    c = int(input("Enter number of columns: "))

    mat = []
    for i in range(r):
        while True:
            row = list(map(int, input(f"Enter row {i+1} elements (space-separated): ").split()))
            if len(row) != c:
                print(f"Error: You must enter exactly {c} elements.")
            else:
                break
        mat.append(row)
    
    target=int(input("Enter an element to find:"))

    if search_an_ele(mat,target):
        print("Element found")
    else:
        print("Not found")