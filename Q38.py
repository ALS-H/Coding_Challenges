"""  Fibonacci Series Pattern (N Rows) 
1 
1 2 
3 5 8 
13 21 34 55 
. 
N rows

"""

def fib_pat(N):
    if N<0:
        raise ValueError("N can't be negative")
    if N==0:
        return 0
    
    #find all fib num
    #pattern needs N(N+1)/2 fibonacci num
    total=N*(N+1)//2
    
    res=[1,1]
    while len(res)<total:
        res.append(res[-1]+res[-2])
    
    idx=0
    for i in range(1,N+1):
        for j in range(1,i+1):
            print(res[idx],end=" ")
            idx+=1
        print()
    

if __name__=="__main__":
    N=int(input("Enter a num:"))
    fib_pat(N)