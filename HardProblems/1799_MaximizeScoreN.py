import math
import collections

nums = [1,2,3,4,5,6]
lenNums = len(nums)
mem = collections.defaultdict(int)

def res(bitwiseMask,count):
    if bitwiseMask in mem:
        return mem[bitwiseMask]
    for i in range(lenNums):
        for j in range(i+1,lenNums):
            if ((1 << i) & bitwiseMask) or ((1 << j) & bitwiseMask):
                continue
            crntScore = count * math.gcd(nums[i],nums[j])
            mem[bitwiseMask] = max(mem[bitwiseMask],crntScore + res((bitwiseMask | (1 << i) | (1 << j)),count+1))
    return mem[bitwiseMask]

print(res(0,1))