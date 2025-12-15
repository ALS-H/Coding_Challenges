# Display the Series 1,4,7,12,23…N

def generate_series(n):
    if n<0:
        raise ValueError("N can't be negative")
    
    if n == 0:
        return []

    series = [1,4,7]
    
    for i in range(4, n):
        series.append(series[-1] + series[-2]+series[-3])

    return series


if __name__ == "__main__":
    n = int(input("Enter number of terms: "))
    print(generate_series(n))
