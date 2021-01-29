# find no. of swaps required to sort the array.

from quickSearch import KthSmallest

def arrayInversion(array):
	temp_array = array.copy()
	counter = 0
	for i in range(len(array)):
		ith_element = KthSmallest(temp_array,0,len(array)-1,i+1)
		if array[i] != ith_element:
			counter = counter + 1
			index = array.index(ith_element)
			array[i],array[index] = array[index],array[i]
	print(array)
	return counter

if __name__ == "__main__":
	array = [2,4,1,3,5]
	#array = [10,10,10]
	#array = [1,2,3,4,5]
	#array = list(map(int,input().split()))
	print(arrayInversion(array))