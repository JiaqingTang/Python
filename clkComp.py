""" method used for comparing vector clock in distributed system course"""

def clkCompare(lista, listb):
	length = len(lista)
	if length != len(listb):
		return -1	
	# -1 for imcomparable, 1 for lista after listb, 0 for lista before listb
	i = 0 #index
	flag = 0 #to help in comparision
	for i in range(length): 
		if(lista[i] >= listb[i]):
			flag += 1;
		else: 
			break
	if flag == length:
		return 1
	flag = 0
	for i in range(length): 
		if(lista[i] <= listb[i]):
			flag -= 1;
		else: 
			break
	if flag == -1 * length:
		return 0
	return -1

# lista = [5,4,0]
# listb = [8,3,0]
# print(clkCompare(lista, listb))