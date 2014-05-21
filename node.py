class node:
	def __init__(self, val):
		self.val = val
		self.next = None

	def getVal(self):
		return self.val
	def getNext(self):
		return self.next

	def setVal(self, val):
		self.val = val
	def setNext(self, next):
		self.next = next

if __name__ == '__main__':

	first = node(2)
	second = node(3)
	first.next = second
	print(first.next.val)