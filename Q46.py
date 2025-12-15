#: Level 1: Find the Sum of all elements in the array

def sum_ele(arr):
    if not arr:
        return None
    return sum(arr)

#test cases
assert sum_ele([1,2,3,4,5])==15
assert sum_ele([-2, -3, -4, 5, 6]) == 2
assert sum_ele([]) == None

print("All test cases passed!")

if __name__=="__main__":
    n=int(input("Enter a num:"))
    arr=[]
    for _ in range(n):
        ele=int(input("Enter an ele:"))
        arr.append(ele)
    print(sum_ele(arr))