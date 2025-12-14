#leap year check
# if it's divisible by 400 or divisible by 4 but not 100
#1900 is divisible by 4 and 100 but not by 400 and it's not a leap year

def leap_year_check(year):
    if year<0:
        raise ValueError("year can't be negative")
    return year%400==0 or (year%4==0 and year%100!=0) #return True or False

#test cases
assert leap_year_check(2024) == True    # divisible by 4, not by 100
assert leap_year_check(2000) == True    # divisible by 400
assert leap_year_check(2023) == False   # not divisible by 4
assert leap_year_check(2100) == False   # divisible by 100, not 400
assert leap_year_check(1900)==False   #div by 4 and 100 but not 400
try:
    leap_year_check(-100)
    assert False
except ValueError:
    assert True

print("All test cases passed!")

if __name__=="__main__":
    year=int(input("Enter an year to check if it's a leap year:"))
    print(leap_year_check(year))     