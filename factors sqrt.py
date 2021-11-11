import math
num=int(input())
for i in range(1,int(math.sqrt(num))+1):
    if(num%i==0):
        d=num//i
        print(i)
        if(d!=i):
            print(d)
