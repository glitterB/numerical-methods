import math
print("Newton Raphson Method")
x1=float(input("\nEnter the Guess: "))
acc=0.00000001

def f(x):
        return (3*x -math.cos(x)- 1)
def fd(x):
        return (3 + math.sin(x))

def newRaph(x):
        while True:
                xn=x-(f(x)/fd(x))
                x=xn
                print(x)
                if abs(f(xn))<acc:
                        break
        print("\nRoot is ",xn)


if abs(f(x1))<abs(fd(x1)):
        print("\nYou may get the root\n")
        newRaph(x1)
else:
        print("Root is far Away")