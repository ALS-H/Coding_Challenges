#program to calculate simple Interest
#P: principal amount, T:time , R:rate of Interest
# S.I=PTR/100

def simple_interest(P,T,R):
    if P<0 or T<0 or R<0:
        raise ValueError("P T R can't be negative values!")
    return round((P*T*R)/100,2)

#test cases
assert simple_interest(1000, 2, 5) == 100.00
assert simple_interest(1000, 0, 10) == 0.00  
assert simple_interest(1_000_000, 10, 12.5) == 1250000.00
# Negative cases (should raise ValueError)
try:
    simple_interest(-1000, 2, 5)
    assert False
except ValueError:
    pass

print("All test cases passed!")

if __name__=="__main__":

    P=float(input("Enter the principal amount:"))
    T=float(input("Enter number of years:"))
    R=float(input("Enter the ROI:"))

    si=simple_interest(P,T,R)
    print("Simple Interest=",si)
