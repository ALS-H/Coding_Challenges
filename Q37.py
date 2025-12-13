""" Printing number Increasing Pattern (N Rows) 
1 
12 
123 
1234 
. 
. 
N rows
"""


def inc_pat3(N):
    if N<0:
        raise ValueError("N can't be negative")
    if N==0:
        return
    for i in range(1,N+1):
        for j in range(1,i+1):
            print(j,end="")
        print()
    

if __name__=="__main__":
    N=int(input("Enter the number of rows:"))
    inc_pat3(N)