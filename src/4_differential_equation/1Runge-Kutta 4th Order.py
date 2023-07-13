def f(x,y):
        return (x*(y**2))

def rk4(x0,y0,xn,n):
        h = (xn-x0)/n
        for i in range (0,n):
                s1 = h *f(x0,y0)
                s2 = h *f((x0+(h/2)),(y0+(s1/2)))
                s3 = h *f((x0+(h/2)),(y0+(s2/2)))
                s4 = h *f((x0+h),(y0+s3))
                s = (s1+(2*s2)+(2*s3)+s4)/6
                y0 = y0 + s
                x0 = x0 + h
                print("Y =",y0)
rk4(0.4,1.72,0.6,1)

