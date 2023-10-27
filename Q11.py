# Q11-accept a number and display whether it is prime or not

# Accept a number from the user.
num = int(input("Enter a number: "))

# Initialize a variable to indicate whether the number is prime.
is_prime = True

# Use a for loop to iterate over all the numbers from 2 to the square root of the input number.
for i in range(2, int(num**0.5) + 1):
  # If any of these numbers divide evenly into the input number, then set is_prime to False and break out of the loop.
  if num % i == 0:
    is_prime = False
    break

# After the loop has finished iterating, check the value of is_prime.
if is_prime:
  print(num, "is a prime number.")
else:
  print(num, "is not a prime number.")