##l=[1,2,3,4,5]
##rotate=int(input())
##for i in range(0,rotate):
##    a=l[0]
##    l.pop(0)
##    l.append(a)
##print(l)

##l=[1,2,3,4,5]
##rotate=int(input())
##for i in range(0,rotate%5):
##    a=l[0]
##    for j in range(1,len(l)):
##        l[j-1]=l[j]
##    l[len(l)-1]=a
##print(l)
    
##l=list(map(int,input().split()))
##rotate=int(input())
##count=0
##for n in l:
##    count+=1
##for i in range(0,rotate%count):
##    a=l[0]
##    for j in range(1,len(l)):
##        l[j-1]=l[j]
##    l[len(l)-1]=a
##print(l)
    
l=list(map(int,input().split()))
rotate=int(input())
count=0
for n in l:
    count+=1
for i in range(0,rotate%len(l)):
    a=l[0]
    for j in range(1,len(l)):
        l[j-1]=l[j]
    l[len(l)-1]=a
print(l)
