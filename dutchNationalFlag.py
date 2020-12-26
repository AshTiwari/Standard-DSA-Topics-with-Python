# Dutch National Flag Algorithm.

# also called Three Way Partition Algorithm.
def dutchNationalFlag(array):
	n = len(array)
	i = 0			# points to the end of sorted subarray of 0s.
	j = 0			# points to the end of sorted subarray of 1s.`
	k = n-1			# points to the end of sorted subarray of 2s from right.
	while(1):
		# traverse until i,j and k are in correct position and pointing unsorted element
		while( i < n-1 and array[i] == 0):
			i = i + 1
		while( j < n-1 and j<i or j < n-1 and array[j] == 1):
			j = j + 1
		while( k>0 and array[k] == 2):
			k = k - 1

		# check for exit condition.
		if (j > k or j == n-1 or k == 0):
			break

		#swap elements to put one of them in correct order.
		if array[j] == 2 and array[k] == 1:
			array[j], array[k] = array[k], array[j]
			j = j+1
			k = k-1
		elif array[i] == 2:
			array[i], array[k] = array[k], array[i]
			k = k-1	
		elif array[i] == 1:
			array[i], array[j] = array[j], array[i]
			j = j+1

	return array


def testDutchNationalFlag():
	test_array = [[2,1,0,0,0,1,2,1,1,2,0,2,1],[0,0,0,0,0],[1,1,1,1,1,1],[2,2,2,2,2,2,2,2],[2,1,2,1,1,1,2,2,2,1],[0,0,0,0,0,1,1,1,1,0,0,1,1,0,1,0,1],[2,2,2,2,0,0,0,0,2,2,0,2,0,2,0,2,0,0]]
	
	for i in range(len(test_array)):
		if i in []:
			continue
		print(dutchNationalFlag(test_array[i]))	

if __name__ == "__main__":
	testDutchNationalFlag()
