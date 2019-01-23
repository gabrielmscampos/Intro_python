def transpor(list_of_lists):
	B = [[] for i in range(len(list_of_lists[0]))]

	for i in range(len(list_of_lists[0])):
		for j in range(len(list_of_lists)):
			B[i].append(list_of_lists[j][i])

	return B

if __name__ == '__main__':
	A = [[0,1,0],[3,5,8],[12,15,55]]
	B = transpor(A)
	print(A)
	print(B)