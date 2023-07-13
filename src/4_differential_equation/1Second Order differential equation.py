def f(x,y,z):
        return ((x+y+z)/y)
    
def g(x,y,z):
        return z

def euler(x,y,z,xn,n):
        h = (xn-x)/n
        for i in range(0,n):
            y1 = y+(h*g(x,y,z))
            z1 = z+(h*f(x,y,z))
            y=y1
            z=z1
            x=x+h
            print('x =',x,', y =',y,', z =',z)
            
def rk2(x,y,z,xn,n):
        h = (xn-x)/n
        for i in range(0,n):
            ys1 = h*(g(x,y,z))
            zs1 = h*(f(x,y,z))
            ys2 = h*(g(x+h,y+ys1,z+zs1))
            zs2 = h*(f(x+h,y+ys1,z+zs1))
            ys = (ys1+ys2)/2
            ys = (zs1+zs2)/2
            y = y+ys
            z = z+zs1
            x =x+h
            print(f"x ={x}, y ={y}, z = {z}")



rk2(0,1,0,0.2,2)
