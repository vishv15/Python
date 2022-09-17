# function that return multiple value


def getResult(num1,num2):
    #Local variable

    addition=num1+num2
    subtraction=num1-num2
    multiplication=num1*num2
    division=num1/num2

    # it will return all 4 variables as tuple which will have addition as first value,
    # subtraction 2 value, multi 3 value, division 4th value
    return addition,subtraction,multiplication,division

    num1=int(input("Enter first number"))
    num2=int(input("Enter second number"))

    #call function
    result = getResult(num1,num2)
    print(result)