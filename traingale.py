h1=int(input("enter h1 :"))
b1=int(input("enter h1 :"))

h2=int(input("enter h2 :"))
b2=int(input("enter h2 :"))

h3=int(input("enter h3 :"))
b3=int(input("enter h3 :"))

t1=h1*b1/2
print(t1)
t2=h2*b2/2
print(t2)
t3=h3*b2/2
print(t3)

if t1>t2 and t1>t3:
    print("t1 is greater")
elif t2>t3 and t2>t1:
    print("t2 is greater")
else:
    print("t3 is greater")