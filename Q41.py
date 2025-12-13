"""  Convert Number to Words Using Mathematical Logic  
a. Input: 270176  
b. Output: Two Seven Zero One Seven Six 

"""

import math

def num_2_word(num):
    if num<0:
        raise ValueError("Enter a positive num!")
    map={0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
    
    res=[]
    while num>0:
        k=num%10
        res.append(map[k])
        num=num//10
    
    res=res[::-1]
    return " ".join(res)

if __name__=="__main__":
    N=int(input("Enter a num:"))
    print(num_2_word(N))