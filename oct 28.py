num=int(input())
n=0
while(num):
    r=num%10
    n=n+(r*r)
    num=num//10
    if(num==0):
        num=n
        n=0
        if(n>=1 and n<=9):
            break
        
if(n==1):
    print("happy number")
else:
    print("not a happy number")
    
    
    
