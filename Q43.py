"""  Whole and Fraction value separation 
Write a program to accept a double value. Separate the whole value from the fractional value and 
store them in two variables. Display the same. 
"""

from decimal import Decimal

def separate_whole_fraction(x):
    d = Decimal(str(x))      # convert safely
    whole = int(d)           # truncates toward 0
    fraction = d - Decimal(whole)
    return whole, fraction
    

#test cases
assert separate_whole_fraction(12.75) == (12, Decimal('0.75'))
assert separate_whole_fraction(-12.753) == (-12, Decimal('-0.753'))
assert separate_whole_fraction(7.0) == (7, Decimal('0.0')) #no fraction

print("All test cases passed!")

if __name__=="__main__":
    num=float(input("Enter a num:"))
    w,f=separate_whole_fraction(num)
    print(w)
    print(f)
