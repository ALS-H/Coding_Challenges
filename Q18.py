#: Display the Series 1,3,5,7,9…N 

def series2(N):
    if N<0:
        raise ValueError("N can't be negative")
    if N==0:
        return []
    num=1
    res=[]
    for i in range(1,N+1):
        res.append(num)
        num+=2
    return res

#test cases
#neg
try:
    series2(-3)
    assert False  # should not reach here
except ValueError:
    assert True

print("All test cases passed!")


if __name__ == "__main__":
    N = int(input("Enter a num: "))
    series = series2(N)
    if series:
        print(*series)  # prints series separated by space
    else:
        print("No numbers to display")