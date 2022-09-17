number=[45,12,78,98,65,32,78,52]
print(number)

user=int(input("Enter your number"))

if user in number:
    print("this number is in list")
    if user %2==0:
        print("this number is even")
    else:
        print("this number is odd")
else:
    print("this number is not in the list")
