a = int(input("this is first number"))
b = int(input("this is second number"))
c = int(input("this is third number"))
if (a<=b) and (a<=c):
    print("this is small number", a)
elif (b<=a) and (b<=c):
    print("this is small number", b)

else :
    print("this is small number", c)

