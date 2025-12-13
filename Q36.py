""" Printing number Increasing Pattern (N Rows) 
1 
22 
333 
4444 
. 
. 
N rows

"""

def inc_pat2(N):
    if N<0:
        raise ValueError("N can't be negative")
    if N==0:
        return
    for i in range(1,N+1):
        print(f"{i}"*i)
    

if __name__=="__main__":
    N=int(input("Enter the number of rows:"))
    inc_pat2(N)