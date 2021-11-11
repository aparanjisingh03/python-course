l=[14,15,2,3,7]
a=[]
for i in range(0,len(l)-1):
    for j in range(i+1,len(l)):
        if(l[i]<l[j]):
            a.append(l[j])
            break
    else:
        a.append(0)
a.append(l[len(l)-1])
print(a)


