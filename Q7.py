#program to accept name and salary. Check if salary>3L and display if they must pay tax

def tax_check(name, salary):
    if salary < 0:
        raise ValueError("Salary can't be negative")
    if salary > 300000:
        return f"{name} has to pay the tax"
    else:
        return f"{name} need not pay tax"

#test cases
assert tax_check("Alice", 500000) == "Alice has to pay the tax"
assert tax_check("Charlie", 300000) == "Charlie need not pay tax"  # exactly 3L
assert tax_check("David", 0) == "David need not pay tax"           # zero salary
try:
    tax_check("Eve", -5000)
    assert False
except ValueError:
    assert True
    
print("All test cases passed!")



if __name__ == "__main__":
    try:
        name = input("Enter your name: ")
        sal = float(input("Enter your salary: "))
        print(tax_check(name, sal))
    except ValueError as e:
        print(e)
