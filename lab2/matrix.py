def transpose(M):
    if len(M) == 0:
        print("fuck u")
        return []
    cols, rows = len(M[0]), len(M)
    return [[M[i][j] for i in range(rows)] for j in range(cols)] # loop cols and rows over rows and cols

                


print(transpose([[],
                 [],
                 []]))