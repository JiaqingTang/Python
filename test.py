def removeABC(str):
	length = len(str)
	i = 0
	while i + 3 < length:
		if str[i: i + 3] == "abc":
			str = str[0: i] + "xy" + str[i + 3: length]
			length -= 1
		i += 1
		print(str)
	return str

if __name__ == '__main__':
	str = "abcacabckek"
	print(removeABC(str))