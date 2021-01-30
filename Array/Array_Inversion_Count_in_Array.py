# two elements are inverted if a[i]>a[j] but i<j.

def nestedLoop(array):
	n = len(array)
	count = 0
	for i in range(n):
		for j in range(i+1,n):
			if array[i] > array[j]:
				count += 1
	return count  

def merge(leftArray, rightArray):
	count = 0
	index1 = index2 = 0
	m = len(leftArray)
	n = len(rightArray)
	#print(m+n)
	sortedArray = []	
	while(index1 < m and index2 < n):
		if leftArray[index1] <= rightArray[index2]:
			sortedArray.append(leftArray[index1])
			index1 += 1 
		elif leftArray[index1] >= rightArray[index2]:
			sortedArray.append(rightArray[index2])			
			index2 += 1
			count += m-index1
	if index1 < m:
		for i in range(index1,m):
			sortedArray.append(leftArray[i])
	elif index2 < n:
		for i in range(index2,n):
			sortedArray.append(rightArray[i])
	##print(f"count = {count}")
	return sortedArray,count

def mergeSort(array,count):
	##print("executing")
	if len(array) <= 1:
		return array,count
	left = 0
	right = len(array)
	mid = (left+right)//2

	leftSubArray, leftCount = mergeSort(array[left:mid],count) 
	rightSubArray, rightCount= mergeSort(array[mid:right],count)
	count += leftCount + rightCount
	array,newCount = merge(leftSubArray,rightSubArray)
	count += newCount
	return array,count

if __name__ == "__main__":
	#array = [2,4,3,1,5]
	#array = [5,2,6,4,7,8,3,1,58,2,9,6,4,8,5,20]	
	#array = list(map(input,input().split()))
	array = [468, 335, 1, 170, 225, 479, 359, 463, 465, 206, 146, 282, 328, 462, 492, 496, 443, 328, 437, 392, 105, 403, 154, 293, 383, 422, 217, 219, 396, 448, 227, 272, 39, 370, 413, 168, 300, 36, 395, 204, 312, 323]
	print("BY Nested Loop:")
	print(nestedLoop(array))
	print("By Recursion:")	
	count = 0
	newArray,count = mergeSort(array,count)
	print(count)
