import math
a = int(input("First Number Input Here"))
b = int(input("Second Number Input Here"))
c = int(input("Third Number Input Here"))
d = (b*b) - (4*a*c)
if(d==0):
    result = -b/(2*a)
    print("Result id", result)
elif(d>0):
    result1 = (-b+math.sqrt(d))/(2*a)
    result2 = (-b-math.sqrt(d))/(2*a)
    print("Result is ", result1,result2)
else:
    print("this number is not supported")

