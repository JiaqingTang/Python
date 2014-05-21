# # def reverseString(str):
# 	# length = len(str) - 1
# 	# for i in range(length / 2):
# 		# tmp = str[length - i]
# 		# str[length - i] = str[i]
# 		str[i] = tmp
# 	# return str
def reverseString(str):
	if len(str) == 1:
		return str
	else:
		return str[len(str) - 1] + reverseString(str[:len(str) - 1])

def reverseString1(str):
	str[::-1]

	return str
print(reverseString1("abcd"))