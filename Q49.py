# Level 4: Search the given element from the array 

def search_ele(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return None

#test cases
assert search_ele([1,2,3,4,5],4)==3
assert search_ele([-25, -13, -4, 56, 67],-13) == 1
assert search_ele([-25, -13, -4, 56, 67],82) == None
assert search_ele([],6) == None

print("All test cases passed!")

if __name__=="__main__":
    n=int(input("Enter a num:"))
    arr=[]
    for _ in range(n):
        ele=int(input("Enter an ele:"))
        arr.append(ele)
    target=int(input("Enter an element to search:"))
    print(search_ele(arr,target))