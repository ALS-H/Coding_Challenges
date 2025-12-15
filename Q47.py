# Level 2: Find the Minimum value of all elements in the array 

def min_ele(arr):
    if not arr:
        return None
    return min(arr)

#test cases
assert min_ele([1,2,3,4,5])==1
assert min_ele([-25, -13, -4, 56, 67]) == -25
assert min_ele([]) == None

print("All test cases passed!")

if __name__=="__main__":
    n=int(input("Enter a num:"))
    arr=[]
    for _ in range(n):
        ele=int(input("Enter an ele:"))
        arr.append(ele)
    print(min_ele(arr))