##def reverse(n):
##    rev=0
##    while(n!=0):
##        r=n%10
##        rev=rev*10+r
##        n=n//10
##    return (rev)
##print(reverse(123))
##
##import math
##def prime_number(n):
##    count=0
##    for i in range(1,n+1):
##        if(n%i==0):
##            count+=1
##    if(count==2):
##       print("prime")
##    else:
##       print("not prime")
##prime_number(7)
##
##def digit_count(n):
##    count=0
##    while(n!=0):
##        n=n//10
##        count+=1
##    print(count)
##digit_count(1278)
##    

def is_prime(n):
    count=0
    for i in range(2,n):
        if(n%i==0):
            return True
        else:
           return False
n=int(input())
if(is_prime(n)):
   print("not prime")
else:
    print(" prime")
