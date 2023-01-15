a = [0,-30,-50,]
b = [50,80,50]
c = [-30,-50,0]
d = [0,0,100]

def upper(a,b,c,d):
        n = len(b)-1
        for i in range(0,n):
                m = a[i+1]/b[i]
                b[i+1] = b[i+1] - m*c[i]
                d[i+1] = d[i+1] - m*d[i]
def back(a,b,c,d):
        upper(a,b,c,d)
        n = len(b)-1
        x=[]
        x.insert((n),(d[n]/b[n]))
        for i in range(n-1,-1,-1):
                x.insert(i,((d[i]- c[i]*x[i+1]) /b[i]))
        print(x)
back(a,b,c,d)

