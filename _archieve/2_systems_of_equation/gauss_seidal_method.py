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
def seidal(a,c):
        n = len(c)
        x =[0,0,0]
        err = 1
        acc = 0.00001
        for it in range(0,11):
                for i in range(0,n):
                        temp = c[i]
                        for j in range(0,n):
                                if i!=j:
                                        temp = temp - a[i][j]*x[j]
                        err = x[i] = temp/a[i][i]
                        x[i] = temp/a[i][i]
                print("x = ",x[0],",y = ",x[1],"z = ",x[2])
pivot(a,c)
seidal(a,c)
        
        
