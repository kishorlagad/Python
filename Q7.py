# Q7-accept numbers till user enters 0 and display the total of all the numbers entered.

sum=0
while True:
    num = int(input("Enter the number : "))
    sum+=num
    print("sum :",sum )
    if num==0:
        break
print("Total sum",sum)
