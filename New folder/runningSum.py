def runningSum(self, nums: list[int]) -> list[int]:
    runningArr = [nums[0]]
    for i in range(1,len(nums)):
        runningArr.append(runningArr[i-1]+nums[i])
    return runningArr

print(runningSum(0,[1,1,1,1,1,1]))