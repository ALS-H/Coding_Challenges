# Level 1: Reverse the given array.

def rev_arr(arr):
    return arr[::-1]

#test cases
assert rev_arr([10, 20, 30]) == [30, 20, 10]
assert rev_arr([-1, -2, -3, -4]) == [-4, -3, -2, -1]
assert rev_arr([]) == []

print("All test cases passed!")

if __name__=="__main__":
    n=int(input("Enter a num:"))
    arr=[]
    for _ in range(n):
        ele=int(input("Enter an ele:"))
        arr.append(ele)
    print(rev_arr(arr))