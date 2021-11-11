num=10
count_set_bit=0
while(num):
    if(num &1):
        count_set_bit+=1
    num=num>>1
print(count_set_bit) 
