# Find pair of all integers in an array whose sum is equal to a number.

from mergeSort import mergeSort
from binarySearch import binarySearch
from collections import Counter

# O(n^2)
def nestedLoop(array,element):
	count = 0
	n = len(array)
	for i in range(n):
		for j in range(i+1,n):
			if array[i] + array[j] == element:
				#print(f"({array[i]},{array[j]})", end = " ")
				count += 1
	#print(end = "\n")
	return count
# O(nLogn)
def sort(arr,element):
	count = 0
	array = arr.copy()
	n = len(array)
	array = mergeSort(array)
	for i in range(n):
		second_integer = element - array[i]
		second_integer_index, frequency = binarySearch(array[i+1:],second_integer,1)
		if second_integer_index != -1:
			count += frequency
			#for _ in range(frequency):
				# print(f"({array[i]},{second_integer})", end = " ")

	#print(end = "\n")
	return count	

# O(n)
def hashMap(array,element):
	counter = Counter(array)
	count = 0
	for i in array:
		second_integer = element - i
		count += counter[second_integer]
		if i == second_integer and counter[second_integer] >= 1:
			count -= 1
	count = count//2
	return count	

if __name__ == "__main__":
	# a = [48,24,99,51,33,39,29,83,74,72,22,46,40,51,67,37,78,76,26,28,76,25,10,65,64,47,34,88,26,49,86,73,73,36,75,5,26,4,39,99,27,12,97,67,63,15,3,92,90]
	a = [46, 22, 14, 97, 22, 67, 30, 95, 23, 30, 6, 17, 40, 69, 60, 97, 70, 66, 45, 32, 13, 4, 74, 40, 61, 49, 2, 23, 96, 55, 17, 93, 28, 30, 41, 2, 96, 70, 96, 18, 51, 53, 86]
	element = 44
	print(f"Count in Nested Loop Function: {nestedLoop(a, element)}")
	print(f"Count in Sort Function: {sort(a, element)}")
	print(f"Count in HashMap Function: {hashMap(a, element)}")
		