self = 0
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

def spiralOrder(self,matrix):
    l = []
    left,top = 0,0
    right = len(matrix[0])
    bottom = len(matrix)

    while left < right and top < bottom:
        for i in range(left,right):
            l.append(matrix[top][i])
        top += 1

        for i in range(top,bottom):
            l.append(matrix[i][right-1])
        right -= 1

        if not (left < right and top < bottom):
            break

        for i in range(right-1,left-1,-1):
            l.append(matrix[bottom-1][i])
        bottom -= 1

        for i in range(bottom-1,top-1,-1):
            l.append(matrix[i][left])
        left += 1

    return l

print(spiralOrder(self,matrix))