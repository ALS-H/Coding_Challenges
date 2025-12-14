""" Printing Number Pattern (N Rows) 
11111 
22222 
33333 
44444 
. 
. 
N rows
"""

def num_pat(N):
    if N<0:
        raise ValueError("N can't be negative")
    if N==0:
        return
    for i in range(1,N+1):
        print(f"{i}{i}{i}{i}{i}")
    

if __name__=="__main__":
    N=int(input("Enter the number of rows:"))
    num_pat(N)
    