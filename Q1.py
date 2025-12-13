#program to find sum and avg of 2 variables
# x and y are input var , they can be int or float

def calculate_sum_and_avg(x,y):
    res=round(x+y,2) #rounding to 2 decimal points
    avg=round((x+y)/2,2)

    return (res,avg) #returns as a tuple


#test cases
assert calculate_sum_and_avg(0,0)==(0.0,0.0)
assert calculate_sum_and_avg(0,10)==(10.0,5.0)
assert calculate_sum_and_avg(-5, -15)==(-20.0,-10.0)
assert calculate_sum_and_avg(-10, 20)==(10.0,5.0)
assert calculate_sum_and_avg(2.5, 7.5)==(10.0,5.0)
assert calculate_sum_and_avg(0.1, 0.2)==(0.3,0.15)
#very large number
assert calculate_sum_and_avg(1000000000000, 1000000000000)==(2000000000000.0,1000000000000.0)
#very small number
assert calculate_sum_and_avg(1e-10, 1e-10)==(0.0,0.0)

print("All test cases passed!")

if __name__=="__main__":    
    
    x=float(input("Enter a num x:"))
    y=float(input("Enter a num y:"))

    ans1,ans2=calculate_sum_and_avg(x,y)
    print("Sum=",ans1)
    print("Avg=",ans2)

    

