import heapq

def maxScore(self,nums1: list[int],nums2: list[int],k: int) -> int:
	nums1 = [x for _, x in sorted(zip(nums2, nums1),reverse=True)]
	nums2.sort(reverse=True)

	knums = [nums1[i] for i in range(k)]
	heapq.heapify(knums)
	maxScoreValue = nums2[k-1] * sum(knums)

	for i in range(k,len(nums1)):
		heapq.heappush(knums,nums1[i])
		heapq.heappop(knums)		
		cntMaxScore = nums2[i] * sum(knums)
		maxScoreValue = max(maxScoreValue,cntMaxScore)

	return maxScoreValue



	


nums1 = [4,2,3,1,1]
nums2 = [7,5,10,9,6]
k = 1

print(maxScore(0,nums1,nums2,k))