# Display the Series 1,5,9,13,21,25,29,37,41…N 
#differences are [+4,+4,+4,+8]->[+4,+4,+8]->[+4,+8]->[+8]

def gen_ser(N):
    if N < 0:
        raise ValueError("N can't be negative")
    if N == 0:
        return []

    series = [1]
    step = 4          # start: every 4th term has +8
    counter = 1       # counts terms since last +8

    while len(series) < N:
        if counter == step:
            series.append(series[-1] + 8)
            counter = 1
            if step > 1:
                step -= 1      # 4 → 3 → 2 → 1
        else:
            series.append(series[-1] + 4)
            counter += 1

    return series


if __name__ == "__main__":
    n = int(input("Enter a num: "))
    print(gen_ser(n))
