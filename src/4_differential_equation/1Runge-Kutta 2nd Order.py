def f(x,y):
        return ((x**2+y**2)**0.5)

def rk2(x0,y0,xn,n):
        h = (xn-x0)/n
        for i in range (0,n):
                s1 = h *f(x0,y0)
                s2 = h *f((x0+h),(y0+s1))
                s = (s1+s2)/2
                y0 = y0 + s
                x0 = x0 + h
                print("Y =",y0)
rk2(1,0,1.3,3)

