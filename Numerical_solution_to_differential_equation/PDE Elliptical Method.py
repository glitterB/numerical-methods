import numpy as np

def laplace(l,n):
        h = l/n;
        tl = int(input("Enter the Left Boundry Condition: "));
        tr = int(input("Enter the Right Boundry Condition: "));
        tb = int(input("Enter the Bottom Boundry Condition: "));
        tt = int(input("Enter the Top Boundry Condition: "));

        t = np.zeros((4, 4))
        for j in range(1,n):
                t[j,0] = tl;
                t[j,n] = tr
                
        for i in range(1,n):
                t[0,i] = tt;
                t[n,i] = tb;
        print(t);

        for itr in range(0,100):
                for i in range(1,n):
                        for j in range(1,n):
                                t[i,j] = (t[i+1,j]+t[i-1,j]+t[i,j+1]+t[i,j-1])/4;
        print('Answer :\n',t);






laplace(3,3)
