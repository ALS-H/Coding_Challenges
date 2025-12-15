#Create a program to compute the sum of all elements in a 2D array.

def sum_all_ele(mat):
    res=0
    for row in mat:
        res+=sum(row)
    return res

#positive cases
assert sum_all_ele([[1, 2], [3, 4]]) == 10
assert sum_all_ele([[5]]) == 5
#negative cases
# Non-numeric value
try:
    sum_all_ele([[1, 2], ["a", 3]])
    assert False
except TypeError:
    assert True
    
#edge cases
assert sum_all_ele([[], []]) == 0     # multiple empty rows

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

    print("Sum of all elements:", sum_all_ele(mat))

