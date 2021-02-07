# Search an element in a matrix which is sorted by rows.

from binarySearch import lessThanEqualBinarySearch

def binarySearch(matrix, m, n, element):
	i = j = 0
	row_begs = [matrix[i][0] for i in range(m)]
	row_no = lessThanEqualBinarySearch(row_begs, element)
	if row_no != -1:
		for i in range(0,n):
			if matrix[row_no][i] == element:
				return (row_no, i)
	return (-1,-1)		

if __name__ == "__main__":
	matrix = [[i + j*5 for i in range(1, 6)] for j in range(5)]
	m = n = 5
	for element in range(27):                              
		print(binarySearch(matrix, m, n, element))