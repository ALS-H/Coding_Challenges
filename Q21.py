# Display the Series 1,4,9,25,36,49,81…N 
#squares

def squares(N):
    if N<0:
        raise ValueError("N can't be negative")
    if N==0:
        return []
    res=[]
    for i in range(1,N+1):
        res.append(i*i)
    return res

#test cases
#neg
try:
    squares(-5)
    assert False  # should not reach here
except ValueError:
    assert True

print("All test cases passed!")


if __name__ == "__main__":
    N = int(input("Enter a num: "))
    series = squares(N)
    if series:
        print(*series)  # prints series separated by space
    else:
        print("No numbers to display")