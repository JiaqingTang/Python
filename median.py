import heapq

class FindMedian:
	def __init__(self):
		self.minHeap, self.maxHeap = [], []

	# maintain two heaps, min heap size always >= max heap size
	# result will be the head from greater size or mean of two heads if 
	# sizes are equal.
	def insert(self, num):
		if len(self.maxHeap) == 0 or num < (self.maxHeap[0] * -1):
			heapq.heappush(self.maxHeap, - 1 * num)
		else:
			heapq.heappush(self.minHeap, num)
		# keep diff of size <= 1
		if abs(len(self.maxHeap) - len(self.minHeap)) > 1:
			if len(self.maxHeap) > len(self.minHeap):
				heapq.heappush(self.minHeap, -1 * heapq.heappop(self.maxHeap))
			else:
				heapq.heappush(self.maxHeap, -1 * heapq.heappop(self.minHeap))

	def getMedian(self):
		if len(self.maxHeap) < 0:
			return
		print self.maxHeap
		print self.minHeap
		if len(self.maxHeap) == len(self.minHeap):
			return (self.maxHeap[0]  * -1 + self.minHeap[0]) / 2.0
		elif len(self.maxHeap) > len(self.minHeap):
			return self.maxHeap[0]
		else:
			return self.minHeap[0]

findMedain = FindMedian()
findMedain.insert(1)
findMedain.insert(0)
findMedain.insert(2)
print findMedain.getMedian()
findMedain.insert(3)
print findMedain.getMedian()