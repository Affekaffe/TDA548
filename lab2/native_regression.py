from matrix import *
import sys
import matplotlib.pyplot as plt

def main():

    file = sys.argv[1]
    M = loadtxt(file)
    X = [M[i][0] for i in range(0,len(M))]
    Y = [M[i][1] for i in range(0,len(M))]

    Xp  = powers(X,0,1)
    Yp  = powers(Y,1,1)
    Xpt = transpose(Xp)

    [[b],[m]] = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))
    print(b,m)

    Y2 = [b + m*x for x in X]

    plt.plot(X,Y,"ro")
    plt.plot(X,Y2)
    plt.show()


main()