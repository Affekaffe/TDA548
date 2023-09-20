def transpose(M):
    if len(M) == 0: # Check for empty matrix
        return []
    rows, cols = len(M), len(M[0])
    return [[M[j][i] for j in range(rows)] for i in range(cols)] # returns matrix with switched ids: new_M[i][j] = M[j][i]

def powers(nlist, n1, n2):
    return [[n**i for i in range(n1,n2+1)] for n in nlist] # powers from n1 to n2 for each n in nlist

def matmul(M1, M2):
    M2_t = transpose(M2) # rows of M2_t = cols of M2 (easier to get row from matrix than col)
    rows, cols = len(M1), len(M2_t)
    prod_M = [[0 for _i in range(cols)] for _j in range(rows)] # init new matrix

    for i in range(rows):
        for j in range(cols):
            prod_M[i][j] = sum(map(lambda a,b: a*b, M1[i], M2_t[j])) # sum ith and jth row of M1 and M2_t

    return prod_M

def invert(M):
    [[a, b],[c,d]] = M
    det = a*d - b*c # determinant
    return [[d/det,-b/det],[-c/det, a/det]]

# loads matrix from txt
def loadtxt(path): 
    file = open("lab2/"+path)
    lines = file.readlines()

    M = []
    for l in lines:
        new_row = [float(n) for n in l.split()] # split into rows
        M.append(new_row)
    
    return M