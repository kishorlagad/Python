# Q4-Display numbers from 3 to 30 except number 24  using while loop.

num=3
while num<31:
    num += 1
    if (num==24):
        continue
    else:
        print(num)