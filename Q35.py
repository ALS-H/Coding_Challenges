""" Printing * Increasing Pattern (N Rows) 
* 
** 
*** 
**** 
. 
. 
N rows
"""

def inc_pat(N):
    if N<0:
        raise ValueError("N can't be negative")
    if N==0:
        return
    for i in range(1,N+1):
        print("*"*i)
    

if __name__=="__main__":
    N=int(input("Enter the number of rows:"))
    inc_pat(N)