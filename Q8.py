#to find the largest of 3 numbers

def largest_num(x, y, z):
    if x > y:
        if x > z:
            return x
        else:
            return z
    else:
        if y > z:
            return y
        else:
            return z

#test cases
assert largest_num(2, 9, 4) == 9
assert largest_num(-1, -5, -3) == -1
#edge cases
assert largest_num(0, -1, -2) == 0   
assert largest_num(7, 7, 7) == 7  #all equal
assert largest_num(5, 5, 2) == 5  #2 equal

print("All test cases passed!")


if __name__=="__main__":
    x=float(input("Enter a num x:"))
    y=float(input("Enter a num y:"))
    z=float(input("Enter a num z:"))

    largest_num(x,y,z)