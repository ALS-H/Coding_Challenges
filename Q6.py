#to check a number is even or odd
#bit manipulation is faster than %2
# & with 1 and the last bit will be 0 for even and 1 for odd

def even_or_odd(x):
    if x&1:
        return "Odd"
    else:
        return "Even"

#test cases
# Positive test cases
assert even_or_odd(2) == "Even"       # small even number
assert even_or_odd(7) == "Odd"        # small odd number
assert even_or_odd(0) == "Even"       # zero (edge case)

# Negative test cases
assert even_or_odd(-2) == "Even"      # negative even number
assert even_or_odd(-7) == "Odd"       # negative odd number

# Edge test cases
assert even_or_odd(2**63) == "Even"   # very large number
assert even_or_odd(2**63 - 1) == "Odd"# very large odd number

print("All test cases passed!")
