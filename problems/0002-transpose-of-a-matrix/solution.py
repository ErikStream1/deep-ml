def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    
    ROWS = len(a)
    COLS = len(a[0])

    matrixT = [[0 for _ in range(ROWS)] for _ in range(COLS)]
 
    for i in range(COLS):
        for j in range(ROWS):
            matrixT[i][j] = a[j][i]

    return matrixT

    # sol numpy
    # import numpy as np
    # return np.transpose(np.array(a))
