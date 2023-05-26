def twoSum(self,numbers: list[int],target: int) -> list[int]:
	i,j = 0,len(numbers)-1

	#loop through numbers to find two sum
	while(True):
		#Current Sum
		currSum = numbers[i] + numbers[j]

		#Current Sum is less than target
		if(currSum < target):
			i += 1

		# Current Sum is greater than target
		elif (currSum > target):
			j -= 1

		#Current Sum is equal to Target
		else:
			return [i+1,j+1]

#inputs
numbers = [2,7,11,15]
target = 9

print(twoSum(0,numbers,target))