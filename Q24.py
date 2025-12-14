# Display the Series 1,1,2,3,5,8,13,21…N 
#fibonacci series

def fib(N):
    if N<0:
        raise ValueError("N can't be negative")
    if N==0:
        return [0]
    if N==1:
        return [1]
    
    res=[1,1]
    for _ in range(2,N):
        res.append(res[-1]+res[-2])
    
    return res


# Negative test case
try:
    fib(-5)
    assert False
except ValueError:
    assert True

print("All test cases passed!")

