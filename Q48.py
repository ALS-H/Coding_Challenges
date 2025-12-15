#Level 3: Find the Maximum value of all elements in the array 


def max_ele(arr):
    if not arr:
        return None
    return max(arr)

#test cases
assert max_ele([1,2,3,4,5])==5
assert max_ele([-25, -13, -4, 56, 67]) == 67
assert max_ele([]) == None


if __name__=="__main__":
    n=int(input("Enter a num:"))
    arr=[]
    for _ in range(n):
        ele=int(input("Enter an ele:"))
        arr.append(ele)
    print(max_ele(arr))