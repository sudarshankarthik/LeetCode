def maxStrength(self,nums: list[int]) -> int:
	strength = 1
	pos = []
	neg = []
	zer = []
	for i in nums:
		if i > 0:
			pos.append(i)
			strength = strength * i
		elif i < 0:
			neg.append(i * -1)
		else:
			zer.append(i)

	if len(pos) == 0 and len(zer) >= 1:
		return 0
	elif len(pos) == 0 and len(zer) == 0 and len(neg) % 2 == 0:
		for i in neg:
			strength = strength * i * -1
	elif len(neg) % 2 != 0:
		neg.sort()
		for i in range(1,len(neg)):
			strength = strength * neg[i]
	else:
		for i in neg:
			strength = strength * i
	return strength

nums = [-4,-5,-4]
print(maxStrength(0,nums))