##li=[1,0,2,0,1]
##i=0
##len=len(li)
##while(len-1):
##    if(li[i]>=1):
##        x=li.pop(i)
##        li.append(x)
##   
##    else:
##        i+=1
##    len-=1
##while(len-1):
##    if(li[i]>li[i+1]):
##        y=
##print(li)
##    
##    
##
##li=[1,0,2,0,0,1,2]
##i=0
##m=0
##j=len(li)-1
##while(m<=j):
##    if(li[m]==2):
##        li[m],li[j]=li[j],li[m]
##        j-=1
##    elif(li[m]==1):
##        m+=1
##    else:
##        li[i],li[m]=li[m],li[i]
##        i+=1
##        m+=1
##print(li)
li=[3,7,10,16,18]
val=int(input())
for i in range(0,len(li)):
    if(li[i]==val):
        print("found at index: ",i)
        break
else:
    print(-1)
    
    

    
    
