nums = [3,2,4]
target = 6

def twoSum(self,nums: list[int],target:int) -> list[int]:
    diffDist = {}
    for i in range(len(nums)):
        crntDiff = target - nums[i]
        if(crntDiff < 0):
            continue
        if(crntDiff in diffDist):
            print(f'match found\n {i},{diffDist[crntDiff]}')
            return [diffDist[crntDiff],i]
        diffDist[nums[i]] = i

    