from numpy import *
import sys
import matplotlib.pyplot as plt

def powers(nlist, n1, n2):
    return array([[n**i for i in range(n1,n2+1)] for n in nlist]) # powers from n1 to n2 for each n in nlist

def main():

    #open file and convert contents to matrix
    file = sys.argv[1]
    M = loadtxt(file)
    X = [M[i][0] for i in range(0,len(M))]
    Y = [M[i][1] for i in range(0,len(M))]

    #linear regression
    Xp  = powers(X,0,1)
    Yp  = powers(Y,1,1)
    Xpt = transpose(Xp)
    
    [[b],[m]] = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp)) #b,m are the predicted values

    Y2 = [b + m*x for x in X]

    #plot the graphs
    plt.plot(X,Y,"ro")
    plt.plot(X,Y2)
    plt.show()

main()