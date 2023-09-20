from numpy import *
import sys
import matplotlib.pyplot as plt

def powers(nlist, n1, n2):
    return array([[n**i for i in range(n1,n2+1)] for n in nlist]) # powers from n1 to n2 for each n in nlist

def poly(a,x): #computes the value of a polynomial witha a value of x and koefficients of a
    y = 0
    for p, c in enumerate(a): # get powers and coefficients small to big
        y += c*(x**p) 
    return y

def main():

    #open file and convert contents to matrix
    file = sys.argv[1]
    M = loadtxt(file)
    X = [M[i][0] for i, _ in enumerate(M)]
    Y = [M[i][1] for i, _ in enumerate(M)]
    
    n = int(sys.argv[2]) #degree 
    
    #Polynomial regression
    Xp  = powers(X,0,n)
    Yp  = powers(Y,1,1)
    Xpt = Xp.transpose()

    a = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
    a = a[:,0] # gives a list of coefficients

    X2 = linspace(min(X),max(X),1000).tolist() # make curvy
    Y2 = [poly(a,x) for x in X2] # calc polynomial value for all inputs

    #plot the graphs
    plt.plot(X,Y,"ro")
    plt.plot(X2,Y2)
    plt.show()

main()