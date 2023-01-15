import numpy as np

a=float(input("Enter value of a: "))
lambd=float(input("Enter value of Lambda: "))
xn=int(input("Enter Length of X: "))
tn=int(input("Enter Length of T: "))
h=float(input("Enter value of h: "))
bcL=float(input("Enter Left Boundry Condition: "))
bcR=float(input("Enter Right Boundry Condition: "))
xt=np.zeros((tn+2,xn+2))
k=lambd*a*h**2

def f(x): 
        return x*(4-x)
for i in range(0,xn+2):
        xt[i,1]=bcL
        xt[i,xn+1]=bcR
        
for j in range(0,xn+1):
        xt[0,j+1]=j
        
for k in range(1,tn+2):
        xt[k][0]=k-1
        
for l in range(0,len(xt[0])-1,1):
        xt[1,l]=f(xt[0,l])
        
for m in range(2,len(xt)):
        for n in range(2,len(xt[0])-1):
                xt[m,n]=lambd*(xt[m-1,n-1]+xt[m-1,n+1])
print(xt)
