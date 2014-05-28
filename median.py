class findMedian:
	def __init__(self):
		self.minHeap, self.maxHeap = [], []
		self.num = 0

	def insert(self, num):
		if self.num % 2 == 0:
			heapq.heappush(self.maxHeap, - 1 * num)
			self.num += 1
			if len(self.minHeap) == 0:
				return
			if -1 * self.maxHeap[0] > self.minHeap[0]:
				toMin = -1 * heapq.heappop(self.maxHeap)
				toMax = heapq.heappop(self.minHeap)