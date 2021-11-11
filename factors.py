import math
num=int(input())
count=2
for i in range(1,int(math.sqrt(num))+1):
    if(num%i==0):
        d=num//i
        if(d==i):
            count+=1
            print(d)
        else:
            count+=2
            print
print(count)
