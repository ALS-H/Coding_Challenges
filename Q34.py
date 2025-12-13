"""  Printing Star Pattern (N Rows) 
***** 
***** 
***** 
***** 
. 
. 
N rows
"""

def star_pat(N):
    if N<0:
        raise ValueError("N can't be negative")
    if N==0:
        return
    for _ in range(N):
        print("*****")
    

if __name__=="__main__":
    N=int(input("Enter the number of rows:"))
    star_pat(N)