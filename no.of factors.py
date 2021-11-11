import math
num=int(input())
count=1
for i in range(1,int(math.sqrt(num))+1):
    if(num%i==0):
        
        count+=2
print(count)
        
