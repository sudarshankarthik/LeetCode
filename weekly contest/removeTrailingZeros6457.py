def differenceOfDistinceValues(self,gird: list[list[int]]) -> list[list[int]]:
	lengthi = len(grid[0])
	lengthj= len(grid)

	ans = [[0 for i in range(lengthi)] for i in range(lengthj)]
	print(ans)

	def getTopLeft(i: int,j: int):
		dig = []
		while i > 0 and j > 0:
			i = i - 1
			j = j - 1
			dig.append(grid[i][j])
		return len(set(dig))

	def getbottomRight(i: int,j: int):
		dig = []
		while i < lengthj-1 and j < lengthi-1:
			i = i + 1
			j = j + 1
			dig.append(grid[i][j])
		return len(set(dig))



	for i in range(lengthj):
		for j in range(lengthi):
			ans[i][j] = abs(getTopLeft(i,j) - getbottomRight(i,j))

	return ans

grid = [[1,2,3],[3,1,5],[3,2,1],[4,5,6]]
print(differenceOfDistinceValues(0,grid))