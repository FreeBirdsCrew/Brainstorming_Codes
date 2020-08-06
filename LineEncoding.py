#For s = "aabbbc", the output should be
#lineEncoding(s) = "2a3bc".

def lineEncoding(s):

	lista = list(s)
	long = len(lista)

	count = 1
	output = ''
	for i in range(long-1):
		if lista[i] != lista[i+1]:
			if count != 1:
				output += str(count) + lista[i]
			else:
				output += lista[i]
			if i == long-2:
				output += lista[i+1]
			count = 1
		else:
			count += 1
			if i == long-2:
				if count != 1:
					output += str(count) + lista[i]
				else:
					output += lista[i]
	return output