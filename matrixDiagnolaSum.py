mat = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
self = 0

def diagonalSum0(self, mat: list[list[int]]) -> int:
    sum = 0
    length = len(mat)
    for i in range(0,length):
        for j in range(0,length):
            if(i == j or (i+j == length-1)):
                print(mat[i][j])
                sum += mat[i][j]
    return sum

def diagonalSum(self, mat: list[list[int]]) -> int:
    sum = 0
    length = len(mat)
    for i in range(length):
        sum += mat[i][i]
        print(length-i-1)
        sum += mat[i][length-i-1]
    if(length%2 != 0):
        sum = sum - mat[length//2][length//2]
    return sum

print(diagonalSum(self,mat))