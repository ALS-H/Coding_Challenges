# Display the Series 4,16,36,64…N 

def series3(N):
    if N<0:
        raise ValueError("N can't be negative")
    if N==0:
        return []
    num=2
    res=[]
    for i in range(1,N+1):
        res.append(num**2)
        num+=2
    return res

#test cases
#neg
try:
    series3(-5)
    assert False  # should not reach here
except ValueError:
    assert True

print("All test cases passed!")


if __name__ == "__main__":
    N = int(input("Enter a num: "))
    series = series3(N)
    if series:
        print(*series)  # prints series separated by space
    else:
        print("No numbers to display")