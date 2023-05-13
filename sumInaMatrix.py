def matrixSum(self, nums: list[list[int]]):
    score =  0
    while(len(nums) != 0):
        maxArr = []
        for row in nums:
            if(len(row) == 0):
                nums.pop(nums.index(row))
                continue
            maxIndex = row.index(max(row))
            maxArr.append(row.pop(maxIndex))
        if(len(maxArr) > 0):
            score +=  max(maxArr)

    return score

print(matrixSum(1,[[7,2,1],[6,4,2],[6,5,3],[3,2,1]]))