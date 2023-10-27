#Q10 -display prime numbers from 3 to 30

for i in range(3,31):
    for j in range(2,i):
        if i%j==0:
            flag=0
            break
        else:
            flag=1
    if(flag==1):
        print(i)
