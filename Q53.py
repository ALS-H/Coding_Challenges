# Level 2: Sort the array in ascending or descending order based on input of user

def sort_arr(arr,instr):
    if instr.lower()=="asc":
        return sorted(arr)
    elif instr.lower()=="desc":
        return sorted(arr,reverse=True)
    else:
        return arr

#test cases
#positive
assert sort_arr([5, 2, 9, 1], "asc") == [1, 2, 5, 9]
assert sort_arr([-1, -3, -2, -5], "desc") == [-1, -2, -3, -5]
#invalid instruction, negative case
assert sort_arr([3, 1, 2], "xyz") == [3, 1, 2]
assert sort_arr([3, 1, 2], "") == [3, 1, 2]
#edge case
assert sort_arr([], "asc") == []
assert sort_arr([], "desc") == []

print("All test cases passed!")

if __name__=="__main__":
    n=int(input("Enter a num:"))
    arr=[]
    for _ in range(n):
        ele=int(input("Enter an ele:"))
        arr.append(ele)
    instr=input("Enter asc/desc:")
    print(sort_arr(arr,instr))