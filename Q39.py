"""  Printing Pattern of Perfect Squares with Alternating Signs in N 
Rows 
1 
-4 9 
-16 25 -36 
49 -64 81 -100 
. 
N rows

"""

def alt_squares(N):
    if N<0:
        raise ValueError("N can't be negative")
    if N==0:
        return
    num=1
    rev=False
    for i in range(1,N+1):
        for _ in range(1,i+1):
            if not rev:
                print(num**2,end=" ")
                num+=1
                rev=True
            else:
                print(-num**2,end=" ")
                num+=1
                rev=False
        print()
    

if __name__=="__main__":
    N=int(input("Enter the number of rows:"))
    alt_squares(N)