# Merge two sorted array in O(1) time.

from binaryInsertion import binaryInsertion
######### Increase the Efficiency by using binaryInsertion function to add element in sorted arr2 ###########

def addElement(arr,element):
	index = 0
	
	# alternate way is to use binaryInsertion.
	while(index < len(arr)-1):
		if arr[index] > arr[index+1]:
			arr[index], arr[index+1] = arr[index+1], arr[index]
		index += 1

def swapAndSort(arr1,arr2):
	index1 = 0
	index2 = 0
	while(index1 < len(arr1)): 
		if arr1[index1] > arr2[index2]:
			arr1[index1], arr2[index2] = arr2[index2], arr1[index1]	
			temp_index2 = index2
		addElement(arr2,arr1[index1])
		index1 += 1

if __name__ == "__main__":
	arr1 = [0,8,9,10,15]
	arr2 = [1,3,9,11,14,16]
	swapAndSort(arr1,arr2)
	print(*arr1+arr2)