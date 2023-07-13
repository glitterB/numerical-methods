import math
import time

print("For x²-cos(x),")

i=0
n=50
acc=0.0001

#Guess from User

x1=float(input("\nEnter the First Guess: "))
x2=float(input("Enter the Second Guess: "))
print('\n')

#Given Function
def f(x):
    return x**2 - math.cos(x)

#Bisection
def bisection(x1,x2):
    
    while True:
        x3 = x1-f(x1)*((x1-x2)/(f(x1)-f(x2)))
        if f(x3)*f(x1)<0:
            x2=x3
        else:
            x1=x3
        global i
        i+=1
        print("i:",i,",","x3 is %f and f(x3) is %1.20f"%(x3,f(x3)))

        if(i<=n and abs(f(x3))<acc):
            break

    print("\nRoot is %f and f(x3) is %1.20f"%(x3,f(x3)))


if (f(x1)*f(x2)<0):
    bisection(x1,x2)
else:
    print("\nRoot does not lie in given guess X1 & X2)")

time.sleep(10)

    


