##li=[1,2,3,2,7,8,6,9]
##count=1
##for i in range(0,len(li)-1):
##    if(li[i]>li[i+1]):
##        count+=1
##    
##        
##print(count)

##li=[1,2,3,2,7,8,6,9]
##li.append(-1)
##for i in range(0,len(li)-1):
##        print(li[i],end="")
##        if(li[i]>li[i+1]):
##            print("\n")
##        
        
##l=[1,2,3,2,7,8,6,9]
##s=0
##for i in range(0,len(l)-1):
##    if(l[i]>l[i+1]):
##        print(l[s:i+1])
##        s=i+1
##print(l[s:])

l=[1,2,3,2,7,8,6,9]
s=0
sum=0
for i in range(0,len(l)-1):
    if(l[i]>l[i+1]):
        t=(l[s:i+1])
        sum=sum+(max(t)-min(t))
        s=i+1
n=l[s:]
sum+=(max(n)-min(n))
print(sum)
