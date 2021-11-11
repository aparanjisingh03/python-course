###to find maximum
##list=[1,3,5,600,950]
##maximum=list[0]
##for i in range(0,len(list)):
##    if(list[i]>maximum):
##        maximum=list[i]
##print(maximum)
##
###to find minimum    
##list=[1,3,5,600,950]
##minimum=list[0]
##for i in range(0,len(list)):
##    if(list[i]<minimum):
##        minimum=list[i]
##print(minimum)
##    
###to find count
##l=[1,2,3,4,2,5,2,100,99]
##val=2
##count=0
##for i in range(0,len(l)):
##    if(l[i]==val):
##        count+=1
##print(count)



        
        
li=[1,1,1,0,0]
x=0
i=0
len=len(li)
while(len-1):
    if(li[i]==1):
      
       x= li.pop(i)
       li.append(x)
    else:
        x+=1
    len-=1
print(li)
        

##li=[1,0,0,1,0,1]
##i=0
##j=len(li)-1
##while(i<=j):
##    if(li[i]==1 and li[j]==0):
##        li[i],li[j]=li[j],li[i]
##        i+=1
##        j-=1
##    elif(li[i]==0 and li[j]==0):
##        i+=1
##    elif(li[i]==0 and li[j]==1):
##        i+=1
##        j-=1
##    else:
##        j-=1
##print(li)
