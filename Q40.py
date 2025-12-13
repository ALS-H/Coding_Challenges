"""  Printing Pattern of Factorials in N Rows 
1 
1 2 
6 24 120 
. 
N rows
"""

import math

def fact_pat(N):
    if N<0:
        raise ValueError("N can't be negative")
    if N==0:
        return
    num=0
    for i in range(1,N+1):
        for j in range(1,i+1):
            print(math.factorial(num),end=" ")
            num+=1
        print()
    

if __name__=="__main__":
    N=int(input("Enter the number of rows:"))
    fact_pat(N)