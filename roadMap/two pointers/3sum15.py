def threeSum(self, nums: list[int]) -> list[list[int]]:
	nums.sort()
	triplts = []
	length = len(nums)
	for i in range(length-1):
		cnt,nxt = nums[i],nums[i+1]
		if cnt == nxt:
			continue

		l,r = i+1,length - 1
		while l < r:
			tot = cnt + nums[l] + nums[r]
			if tot > 0:
				r -= 1
			elif tot < 0:
				l += 1
			else: # tot == 0
				triplts.append([cnt,nums[l],nums[r]])
				l += 1
	return triplts



nums = [-1,0,1,2,-1,4]
print(threeSum(0,nums))