def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    frequency = []
    counted = []
    for num in nums:
        if num not in counted:
            counted.append(num)
            frequency.append((num,nums.count(num)))
    frequency.sort(key= lambda n:n[1],reverse=True)
    return [frequency[i][0] for i in range(k)]

nums = [1,2,2,2,3,3,4,4,5,6]
k = 2
print(topKFrequent(0,nums,k))