
n = 4

def spiralOrder(self,n):
    matrix = [[0 for x in range(n)] for y in range(n)] 
    top,left = 0,0
    bottom,right = n,n
    val = 1

    while val != n*n+1:
        #left to right
        for i in range(left,right):
            matrix[top][i] = val
            val += 1
        top += 1

        #top to bottom
        for i in range(top,bottom):
            matrix[i][right-1] = val
            val += 1
        right -= 1
        
        #right to left
        for i in range(right-1,left-1,-1):
            matrix[bottom-1][i] = val
            val += 1
        bottom -= 1

        #bottom to top
        for i in range(bottom-1,top-1,-1):
            matrix[i][left] = val
            val += 1
        left += 1
    return matrix

print(spiralOrder(0,n))