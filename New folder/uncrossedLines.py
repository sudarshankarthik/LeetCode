def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
    len1 = len(nums1)
    len2 = len(nums2)
    dp = [[0 for x in range(len1+1)] for y in range(len2+1)]
    for i in range(len1+1):
        for j in range(len2+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif nums1[i-1] == nums2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[len1][len2]

nums1 = [1,4,2]
nums2 = [1,2,3]
print(maxUncrossedLines(1,nums1,nums2))