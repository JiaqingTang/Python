
def reverseString(str):
	if len(str) == 1:
		return str
	else:
		return str[len(str) - 1] + reverseString(str[:len(str) - 1])

def reverseString1(str):
	str[::-1]
	return str

print(reverseString1("abcd"))