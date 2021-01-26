# Find duplicate in an series from 0 to n-1 in O(n) time and O(1) space.
# Note: For every element there is an index equal to that element in this special series.

# for every element, find the index equal to it and change its sign to negative.
def checkSign(arr):
	array = arr.copy()
	for i in array:
		# this solves the problem of printing duplicates for more than one time.
		if array[abs(i)] == None:
			continue 
		elif array[abs(i)] < 0:
			print(abs(i) , end = ' ') 				
			array[abs(i)] = None
		elif array[abs(i)] > 0:
			array[abs(i)] = -array[abs(i)]
	print(end = '\n')

# print the index with value greater than 1  in modified array.
def checkValue(arr):
	array = arr.copy()
	n = len(array)
	for i in array:
		array[i%n] = array[i%n] + n
	for i in range(n):
		if array[i]/n > 2:
			print(i,end = ' ')
#	print('\n')

if __name__ == "__main__":
	array = [1,1,1,2,3,4,2,2,0,8,6,0]
#	array = [0]
	# prints duplicate in the order they occur.
	checkSign(array)
	# prints duplicate in sorted order.
	checkValue(array)