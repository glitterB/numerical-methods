def f(x):
        return 1.5*x +2

def trap(x0,xn,m):
        n=2*m
        a=0
        h=(xn-x0)/n
        for i in range(1,m+1):
                a+=(h/3)*(f(x0)+4*f(x0+h)+f(x0+2*h))
                x0+=2*h
        print(a)
trap(0,1.5,3)
