#Example
#For inputString = "fun", the output -
#alphaShift(inputString) = "gvo".

def alphaShift(inputString):

	alphabet = "abcdefghijklmnopqrstuvwxyz"

	listaAlpha = list(alphabet)

	lista = list(inputString)

	for c in range(len(lista)):

		index = [i for i,x in enumerate(listaAlpha) if x == lista[c]]
		#If it is not a 'z'
		if index[0] != (len(listaAlpha)-1):
			lista[c] = listaAlpha[index[0]+1]
		else:
			# for 'z'
			lista[c] = listaAlpha[0]

	return ''.join(lista)