#program to swap two numbers
#int and float are immutable and cannot be swapped by reference 
#use return

def swap_2_num(x,y):
    return y,x #tuple
    

#test cases 
assert swap_2_num(5, 10) == (10, 5)          # pos
assert swap_2_num(2.5, -3.7) == (-3.7, 2.5)  #neg
assert swap_2_num(1e308, -1e308) == (-1e308, 1e308) #very large numbers
assert swap_2_num(float('inf'), float('-inf')) == (float('-inf'), float('inf'))

print("All test cases passed!")

def parse_number(s):
    num = float(s)
    if num.is_integer():  # check if it’s a whole number
        return int(num)
    return num

if __name__ == "__main__":
    try:
        x = parse_number(input("Enter a num x: "))
        y = parse_number(input("Enter a num y: "))
        print("Before swap: X =", x, "Y =", y)
        x, y = swap_2_num(x, y)
        print("After swap:  X =", x, "Y =", y)
    except ValueError:
        print("Invalid input! Please enter numeric values.")

    