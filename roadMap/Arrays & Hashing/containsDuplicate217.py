def containsDuplicate(self,nums: list[int]) -> bool:
    if len(nums) == len(set(nums)):
        return False
    return True

nums = [1,2,1]
print(containsDuplicate(0,nums))