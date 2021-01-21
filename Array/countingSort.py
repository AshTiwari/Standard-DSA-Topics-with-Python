# Implementing Counting Sort.

def countingSort(array,start,end):
	sorted_array = []
	count_dict = {}
	for i in array:
		count_dict[i] = count_dict.get(i,0) + 1
	for i in range(start,end+1):
		for j in range(count_dict.get(i,0)):
			sorted_array.append(i)
	return sorted_array	


def countingSortInPlace(array,start,end):
	return 0


def testCountingSort():
	test_array = [[2,1,0,0,0,1,2,1,1,2,0,2,1],[0,0,0,0,0],[1,1,1,1,1],[2,2,2,2,2],[2,1,2,1,1,1,2,2,2,1],[0,0,0,0,0,1,1,1,1,0,0,1,1,0,1,0,1],[2,2,2,2,0,0,0,0,2,2,0,2,0,2,0,2,0,0]]
	
	for i in range(len(test_array)):
		print(countingSort(test_array[i],0,2))

if __name__ == "__main__":
	testCountingSort()	
		