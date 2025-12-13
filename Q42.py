# Generate Series : 1, -5, 9, -13, 17, -21, ... N 

def alt_series(N):
    if N<0:
        raise ValueError("N should be positive")
    if N==0:
        return
    num=1
    rev=False
    for i in range(N):
        if not rev:
            print(num,end=" ")
            num+=4
            rev=True
        else:
            print(-num,end=" ")
            num+=4
            rev=False
            
if __name__=="__main__":
    N=int(input("Enter a num N:"))
    alt_series(N)