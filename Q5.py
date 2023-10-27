# Q5-accept marks from the user. Using if…….elif….  Else,
# display whether result is  fail, pass, second class , first class,

marks = int(input("Enter Marks : "))

if marks>=75:
    print("First with Distinction ")
elif marks<75 and marks>=50:
    print("Second Class")
elif marks>=35 and marks<50:
    print("Pass")
else:
    print("Fail")