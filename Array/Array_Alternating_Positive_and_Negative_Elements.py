# Rearrange elements in alternating positive and negative elements in O(n) space.

def updatePosIndex(array, pos_index,n,k):
	for index in range(pos_index+k,n):
		if array[index] >= 0:
			pos_index = index
			break
	return pos_index

def updateNegIndex(array, neg_index,n, k):
	for index in range(neg_index+k,n):
		if array[index] < 0:
			neg_index = index
			break
	return neg_index

def twoPointer(array):
#	array = arr.copy()
	n = len(array)
	pos_index = updatePosIndex(array, 0, n, 0)
	neg_index = updateNegIndex(array, 0, n, 0)
	flag = 1
	for i in range(n):
		print(f"index = {i}, pos_index = {pos_index}, neg_index = {neg_index}")
		print(array)
		if flag == 1:
			if array[i] < 0:
				array[i], array[pos_index] = array[pos_index], array[i]
				neg_index = updateNegIndex(array, neg_index,n, 1)
			pos_index = updatePosIndex(array, pos_index,n, 1)
		elif flag == -1:
			if array[i] >= 0:
				array[i], array[neg_index] = array[neg_index], array[i]
				pos_index = updatePosIndex(array, pos_index,n, 1)
			neg_index = updateNegIndex(array, neg_index,n, 1)
		flag = flag*-1
	return array

if __name__ == "__main__":
	array = [9, 4, -2, -1, 5, 0, -5, -3, 2]
	print(twoPointer(array))

# alternate solution would be to shift all negative numbers to end and then use swaps.