#  Level 0: Write a program to accept n and store the elements into the array of size n.

def store_ele(n):
    if n<0:
        raise ValueError("Number of elements can't be negative!")
    if n==0:
        return 
    arr=[0]*n
    
    for i in range(n):
        arr[i]=input("Enter a val:")
    return arr

if __name__=="__main__":
    n=int(input("Enter a num:"))
    res=store_ele(n)
    print(res)