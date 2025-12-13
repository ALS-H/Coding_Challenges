#program to calculate the discount on the total amount

def amount_to_pay(A,D):
    if A<0 or D<0:
        raise ValueError("Amount and Discount can't be negative!")
    if D>100:
        raise ValueError("Discount can't exceed 100!")
    discount=(D/100)*A
    final_amount=round(A-discount,2)
    return final_amount

#test cases
assert amount_to_pay(1000, 10) == 900.0
assert amount_to_pay(0, 10) == 0.0        # zero amount
# Large values
assert amount_to_pay(1_000_000, 25) == 750000.0
#negative test cases
try:
    amount_to_pay(-1000, 10)
    assert False
except ValueError:
    assert True

print("All test cases passed!")

if __name__=="__main__":

    A=float(input("Enter the total amount:"))
    D=float(input("Enter the discount percent:"))
    print(amount_to_pay(A,D))

    