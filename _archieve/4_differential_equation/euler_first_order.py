def f(x,y):
        return x + y**2

def euler(x0,y0,xn,n):
        for i in range(0,n):
                h = (xn - x0)/n
                y0 = y0 + (h*f(x0,y0))
                x0 = x0+h
                print ("Y= ",y0)
        
euler(0,1,0.3,3)

