# Merge two sorted array in O(1) time.

def swapAndSort(arr1,arr2):
	index1 = 0
	index2 = 0
	while(index1 < len(arr1)): # and index2 < len(arr2)):
		if arr1[index1] > arr2[index2]:
			arr1[index1], arr2[index2] = arr2[index2], arr1[index1]	
			temp_index2 = index2
			while(temp_index2 < len(arr2)-1):
				if arr2[temp_index2] > arr2[temp_index2+1]:
					  arr2[temp_index2], arr2[temp_index2+1] = arr2[temp_index2+1], arr2[temp_index2]
				temp_index2 += 1
			
		#if arr1[index1] < arr2[index2]:
			#pass
		index1 += 1

if __name__ == "__main__":
	arr1 = [0,8,9,10,15]
	arr2 = [1,3,9,11,14,16]
	swapAndSort(arr1,arr2)
	print(*arr1+arr2)