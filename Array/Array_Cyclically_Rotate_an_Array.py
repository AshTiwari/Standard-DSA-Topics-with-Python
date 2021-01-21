# cyclically rotate a list.

def cRotate(array):
	n = len(array)
	if n != 0:
		temp = array[0]
	for i in range(1,n):
		temp, array[i] = array[i], temp
	if n != 0:
		array[0] = temp
	return array

def test_cRotate():
	test_array = [[1],[],[1,2,3,4],[1,2,3]]
	for i in test_array:
		print(cRotate(i)) 
		
if __name__ == "__main__":
        test_cRotate()