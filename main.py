N = int(input("enter a number "))

if N>50:
    print("number is greater than 50")
    if N%2==0:
        print("and it is even too")
    else:
        print("and it is odd")
else:
    print("number is less than 50")