arr=[1,2,3,1,2,3]
x=0
for i in range(0,len(arr)-1):
    for j in range(i+1,len(arr)):
        if(arr[i]==arr[j]):
            print(arr[i])
            x+=1
if(x==0):
    print(-1)
    
    
