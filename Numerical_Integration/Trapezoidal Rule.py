def f(x):
        return 1.5*x +2

def trap(x1,x2,m):
        n=m
        a=0
        h=(x2-x1)/n
        for i in range(1,m+1):
                a+=h/2*(f(x1+(i-1)*h)+f(x1+i*h))
        print(a)
trap(1,2,4)
