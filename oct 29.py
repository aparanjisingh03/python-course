##for i in range(1,6):
##    for j in range(1,6):
##        print(j,end=" ")
##    print('\n')

##n=5
##for i in range(1,6):
##     for j in range(1,6):
##        print(n,end=" ")
##     n=n-1
##     print('\n')


##for i in range(1,6):
##    for j in range(1,i):
##        print(j,end=" ")
##    print('\n')
##    
##for i in range(1,6):
##    for j in range(1,i+1):
##        print(i,end=" ")
##    print('\n')


##for i in range(1,6):
##    for k in range(1,6-i):
##              print(" ",end="")
##    for j in range(1,i+1):
##              print(i,end=" ")
##    print('\n')

##for i in range(5,0,-1):
##    for k in range(0,5-i):
##        print(" ",end="")
##    for j in range(1,i+1):
##        print(i,end=" ")
##    print('\n')

n=int(input())
i=1
row_count=0
while True:
    print(i,end=" ")
    i+=1
    if(i==n+1):
        print()
        i=1
        row_count+=1
        if(row_count==n):
            break
