# Find commmon elements in three sorted arrays.

def threePointer(a,ar,arr):
	a_index = ar_index = arr_index = 0
	duplicate = []
	while(a_index < len(a) and ar_index < len(ar) and arr_index < len(arr)):
		maxElement = max(a[a_index],ar[ar_index],arr[arr_index])

		# replace below while loops by using binarySearch.
		while(a_index < len(a) and a[a_index] < maxElement ):
			a_index += 1
		while(ar_index < len(ar) and ar[ar_index] < maxElement ):
			ar_index += 1
		while(arr_index < len(arr) and arr[arr_index] < maxElement):
			arr_index += 1

		if not (a_index < len(a) and ar_index < len(ar) and arr_index < len(arr)):
			break
		if a[a_index] == ar[ar_index] == arr[arr_index]:
			#print(f"{maxElement}", end = " ")
			duplicate.append(maxElement)
			a_index += 1
			ar_index += 1
			arr_index += 1
	return duplicate	

if __name__ == "__main__":
	a = [1, 5]
	ar = [3, 4, 5, 5, 10]
	arr = [5, 5, 10, 20]
	print(threePointer(a,ar,arr))

	