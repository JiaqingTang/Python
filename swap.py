def swap(a, b):
	print(a,b)
	a = a ^ b
	b = a ^ b
	a = a ^ b
	print(a, b)

def convert(num, base):
	table = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f']
	result = []
	while num:
		index = num % base
		result.insert(0, table[index])
		num /= base
	return result
mylist = convert(255,10)
my_ints = map(int, mylist)
print(my_ints)