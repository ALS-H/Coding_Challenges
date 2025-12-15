# Level 3: Implement Binary Search on the array.

def bin_search(arr,target):
    low,high=0,len(arr)-1
    
    while low<=high:
        mid=low+(high-low)//2
        
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1 #not found

#test cases
assert bin_search([2, 4, 6, 8, 10], 10) == 4
assert bin_search([1, 3, 5, 7, 9], 4) == -1
assert bin_search([], 5) == -1
assert bin_search([1, 2, 2, 2, 3], 2) in [1, 2, 3] #duplicate values
assert bin_search([5, 5, 5, 5], 5) in [0, 1, 2, 3]

print("All test cases passed!")

if __name__=="__main__":
    n=int(input("Enter a num:"))
    arr=[]
    for _ in range(n):
        ele=int(input("Enter an ele:"))
        arr.append(ele)
    target=int(input("Enter an element to search:"))
    res=bin_search(arr,target)
    
    if res<0:
        print("not found")
    else:
        print("Found at:",res)