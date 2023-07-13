a = [[4,7,1,],
    [2,3,4],
    [6,2,7],]

c = [7,9,15]

def pivot(a,c):
        n = len(c)
        for i in range(0,n):
                for j in range(i+1,n):
                        if abs(a[j][i])>abs(a[i][i]):
                                for k in range (0,n):
                                        temp = a[i][k]
                                        a[i][k] = a[j][k]
                                        a[j][k] = temp
                                temp = c[i]
                                c[i] = c[j]
                                c[j] = temp


def upper(a,c):
        n = len(c)
        for i in range(0,n):
                for j in range(i+1,n):
                        r = a[j][i]/a[i][i]
                        for k in range (0,n):
                                a[j][k] =a[j][k] - (r*a[i][k])
                        c[j] = c[j] -(r*c[i])


def back(a,c):
        pivot(a,c)
        upper(a,c)
        n = len(c) - 1
        x = []
        for i in range(n,-1,-1):
                temp = c[i]
                if i ==0 or i ==1:
                        for j in range (i+1,(n),1):
                                        temp = temp - (a[i][j]*x[i])
                x.insert(i,(temp / a[i][i]))
        
        return x

x= back(a,c)
print(x)
