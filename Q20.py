# Display the Series 1,2,4,7,11,16,22…N 
#differences are 1,2,3,4,5...

def series4(N):
    if N<0:
        raise ValueError("N can't be negative")
    if N==0:
        return []
    num=1
    res=[]
    for i in range(0,N):
        num+=i
        res.append(num)
    return res

#test cases
#neg
try:
    series4(-5)
    assert False  # should not reach here
except ValueError:
    assert True

print("All test cases passed!")


if __name__ == "__main__":
    N = int(input("Enter a num: "))
    series = series4(N)
    if series:
        print(*series)  # prints series separated by space
    else:
        print("No numbers to display")