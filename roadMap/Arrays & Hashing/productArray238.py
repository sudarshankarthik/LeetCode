def productExceptSelf(self, nums: list[int]) -> list[int]:
    
    out = [1]

    for i in range(len(nums)-1):
        out.append(out[i]*nums[i])
    
    postFix = 1
    for i in range(len(nums)-1,-1,-1):
        out[i] = out[i] * postFix
        postFix = nums[i] * postFix

    return out

print(productExceptSelf(0,[-1,1,0,-3,3]))