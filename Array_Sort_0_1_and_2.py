# sort an array of 0s, 1s and 2s.
from countingSort import countingSort
from dutchNationalFlag import dutchNationalFlag

def countingSortMethod(array):
	return countingSort(array,0,2)
	
# also called Dutch Nationala Flag Algorithm.
def threeWayPartition(array):
	return dutchNationalFlag(array)

if __name__ == "__main__":
	array = [2,1,0,0,0,1,2,1,1,2,0,2,1]
	print(countingSortMethod(array))
	print(threeWayPartition(array))
