def longestConsecutive(self,nums: list[int]) -> int:
	longestLen = 1
	nums.sort()
	crntLen = 1
	for i in range(1,len(nums)):
		if nums[i-1] + 1 == nums[i]:
			crntLen += 1
		else:
			longestLen = max(longestLen,crntLen)
			crntLen = 1

	return max(longestLen,crntLen)

nums =[0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(0,nums))