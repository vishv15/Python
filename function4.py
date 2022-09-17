#Exampale of with return value without argument function
from multiprocessing.heap import Arena


def getpi():
    pi=3.14  # local variable
    return pi # This function return value of pi variable which is 3.14

# With return value with argument function
def getsquare(number):
    square=number*number # local variable
    return square

radius=float(input("Enter radius"))
pi=getpi()

# calculate area formula pi * r * r
square=getsquare(radius)
Area=pi*square
print(Area)