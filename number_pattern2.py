"""  Printing Number Pattern (N Rows) 
12345 
12345 
12345 
12345 
. 
. 
N rows
"""

def num_pat2(N):
    if N<0:
        raise ValueError("N can't be negative")
    if N==0:
        return
    for _ in range(N):
        print("12345")
    

if __name__=="__main__":
    N=int(input("Enter the number of rows:"))
    num_pat2(N)