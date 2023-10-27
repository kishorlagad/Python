# Q8- accept a character and display whether it is upper case or lower case or not an alphabet.

ch = ord(input("Enter Alphabet : "))

if ch>=ord('A'):
    if ch<=ord('Z'):
        print("Upper Case")

    if ch >= ord('a'):
        if ch <= ord('z'):
            print("Lower Case")
else:
    print("Bhag")