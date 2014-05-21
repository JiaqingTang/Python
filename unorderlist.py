from node import node
class unorderlist:
	def __init__(self):
		self.head = None
		self.count = 0
	def isEmpty(self):
		return self.head == None
	def add(self, val):
		tmp = node(val)
		tmp.setNext(self.head)
		self.head = tmp 
		self.count += 1
	def getSize(self):
		return self.count
	def search(self, val):
		cur = self.head
		while cur and cur.val != val:
			cur = cur.next 
		if not cur:
			return False
		else:
			return True
	def remove(self, val):
		if not self.search(val):
			return
		else:
			cur = self.head
			if cur.val == val:
				self.head = cur.next
			else:

				while cur.next and cur.next.val != val:
					cur = cur.next
				cur.next = cur.next.next




mylist = unorderlist()
mylist.add(3)
mylist.add(2)
mylist.add(4)
print(mylist.head.next.val)
print(mylist.search(4))
mylist.remove(4)
print(mylist.search(4))
