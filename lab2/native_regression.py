from matrix import *
import sys
import matplotlib.pyplot as plt

def main():

    #open file and convert contents to matrix
    file = sys.argv[1]
    M = loadtxt(file)
    X = [M[i][0] for i, _ in enumerate(M)]
    Y = [M[i][1] for i, _ in enumerate(M)]

    #linear regression
    Xp  = powers(X,0,1)
    Yp  = powers(Y,1,1)
    Xpt = transpose(Xp)

    [[b],[m]] = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp)) #b,m are the predicted values

    Y2 = [b + m*x for x in X]

    #plot the graphs
    plt.plot(X,Y,"ro")
    plt.plot(X,Y2)
    plt.show()


main()