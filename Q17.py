#Display the Series 1,2,3,4,5,6…N 

def series1(N):
    if N<0:
        raise ValueError("N should be positive")
    if N == 0:
        return []
    return list(range(1, N + 1))

# Positive test cases
assert series1(5) == [1, 2, 3, 4, 5]
assert series1(0) == []        # N = 0
#neg
try:
    series1(-3)
    assert False  # should not reach here
except ValueError:
    assert True

print("All test cases passed!")


if __name__ == "__main__":
    N = int(input("Enter a num: "))
    series = series1(N)
    if series:
        print(*series)  # prints series separated by space
    else:
        print("No numbers to display")
