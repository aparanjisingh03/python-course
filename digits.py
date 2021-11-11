num=int(input())
even_count=0
odd_count=0
digit_count=0
while(num!=0):
    digit_count+=1
    r=num%10
    if(r%2==0):
        even_count+=1
    else:
        odd_count+=1
    num=num//10
##if(even_count>odd_count):
##    print("strongly even")
##elif(even_count==odd_count):
##    print("strongly odd")
##else:
##    print("neutral")
if(even_count==digit_count):
     print("strongly even")
elif(odd_count==digit_count):
    print("strongly odd")
else:
    print("neutral")
