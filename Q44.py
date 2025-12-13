"""  Reverse of a number 
Write a program to find the reverse of a number. Store the reverse value in a different variable. 
Display the reverse.
"""

def rev_num(num):
    sign=-1 if num<0 else 1
    num=abs(num)
    
    if num==0:
        return 0
    
    rev=""
    while num>0:
        k=num%10
        rev+=str(k)
        num=num//10
    
    return sign*int(rev)

#test cases
assert rev_num(123) == 321
assert rev_num(10) == 1
assert rev_num(-123) == -321
assert rev_num(-10) == -1
assert rev_num(-5) == -5

print("All test cases passed!")