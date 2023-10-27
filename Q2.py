# Q2-using switch ….case   display whether accepted character is vowel or not.


ch= input("Enter vowel : ")

match ch:
    case 'a':
        print("a is vowel")
    case 'e':
        print("e is vowel")
    case 'o':
        print("o is vowel")
    case 'i':
        print("i is vowel")
    case 'u':
        print("u is vowel")
    case _ :
        print("char is not vowel")