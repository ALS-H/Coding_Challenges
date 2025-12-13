"""  Whole and Fraction value separation 
Write a program to accept a double value. Separate the whole value from the fractional value and 
store them in two variables. Display the same. 
"""

def separate_whole_fraction(x):
    """
    Returns (whole_part, fractional_part)
    """
    whole = int(x)          # truncates toward zero
    fraction = x - whole
    return whole, fraction

#test cases
assert separate_whole_fraction(12.75) == (12, 0.75)
assert separate_whole_fraction(-12.75) == (-12, -0.75)
assert separate_whole_fraction(7.0) == (7, 0.0) #no fraction

print("All test cases passed!")
