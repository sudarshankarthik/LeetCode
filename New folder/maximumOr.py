def check(nums, k, mid):
    # Count the number of operations required to make all elements >= mid
    cnt = 0
    for num in nums:
        cnt += (mid - num + 1) // 2
        if cnt > k:
            return False
    return True

def maximum_or(nums, k):
    # Find the maximum value in the array
    max_num = max(nums)
    # Binary search for the maximum possible value
    left, right = 0, max_num
    while left < right:
        mid = (left + right + 1) // 2
        if check(nums, k, mid):
            left = mid
        else:
            right = mid - 1
    return left

# Example usage
nums = [12,9]
k = 1
print(maximum_or(nums, k))  # Output: 7
