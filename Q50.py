# Level 5: Display the number of odd and even numbers from the array

def odd_even_count(arr):
    if not arr:
        return None
    odd_cnt,even_cnt=0,0
    for num in arr:
        if num%2==0:
            even_cnt+=1
        else:
            odd_cnt+=1
    return odd_cnt,even_cnt

#test cases
assert odd_even_count([1, 2, 3, 4, 5]) == (3, 2)
assert odd_even_count([2, 4, 6, 8]) == (0, 4)
assert odd_even_count([1, 3, 5, 7]) == (4, 0)
assert odd_even_count([-1, -2, -3, -4]) == (2, 2)
assert odd_even_count([0, -1, 2, -3, 4]) == (2, 3)
assert odd_even_count([7]) == (1, 0)
assert odd_even_count([10]) == (0, 1)
assert odd_even_count([]) is None
print("All test cases passed!")

if __name__=="__main__":
    n=int(input("Enter a num:"))
    arr=[]
    for _ in range(n):
        ele=int(input("Enter an ele:"))
        arr.append(ele)
    o,e=odd_even_count(arr)
    print("Odd count:",o)
    print("Even count",e)