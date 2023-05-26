import heapq

class KthLargest:

	def __init__(self,k: int,nums: list[int]):
		self.k = k
		self.heap = nums
		heapq.heapify(self.heap)
		if len(self.heap) < self.k:
			heapq.heappush(self.heap,-100000)
		while len(self.heap) > k:
			heapq.heappop(self.heap)

	def add(self,val: int) -> int:
		if val < self.heap[0]:
			return self.heap[0]
		heapq.heappush(self.heap,val)
		heapq.heappop(self.heap)
		return self.heap[0]


k = 3
nums = [4,5,8,2]

kthLargest = KthLargest(k,nums)
print(kthLargest.add(3))
print(kthLargest.add(5))
print(kthLargest.add(10))
print(kthLargest.add(9))
print(kthLargest.add(4))