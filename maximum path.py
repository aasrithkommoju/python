# Python 3 prorgam for finding max path in matrix 
# To calculate max path in matrix 
  
def findMaxPath(mat): 
  
    # To find max val in first row 
    res = -1
    for i in range(M): 
        res = max(res, mat[0][i]) 
   
    for i in range(1, N): 
   
        res = -1
        for j in range(M): 
   
            # When all paths are possible 
            if (j > 0 and j < M - 1): 
                mat[i][j] += max(mat[i - 1][j], 
                                 max(mat[i - 1][j - 1],  
                                     mat[i - 1][j + 1])) 
   
            # When diagonal right is not possible 
            elif (j > 0): 
                mat[i][j] += max(mat[i - 1][j], 
                                 mat[i - 1][j - 1]) 
   
            # When diagonal left is not possible 
            elif (j < M - 1): 
                mat[i][j] += max(mat[i - 1][j], 
                                 mat[i - 1][j + 1]) 
   
            # Store max path sum 
            res = max(mat[i][j], res) 
    return res 
  
# Driver program to check findMaxPath 
N=3
M=4
mat = ([[ 5, 1, 2, 6 ], 
        [ 9, 9, 7, 5 ], 
        [ 3, 1, 4, 8 ]]) 
                
print(findMaxPath(mat)) 
