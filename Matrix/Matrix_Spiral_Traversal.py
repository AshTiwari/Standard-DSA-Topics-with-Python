# Print a matrix in spiral form.

def simpleSolution(matrix, m, n):
	rowIndex = colIndex = 0
	# m represents row number which we shouldn't touch.
	# n represents col number which we shouldn't touch.
	while(rowIndex < m and colIndex < n):
		# increase rowIndex or decrease m.
		# increase colIndex or decrease n.
		
		# print row from left to right.
		for i in range(colIndex,n):
			print(matrix[rowIndex][i])
		rowIndex += 1

		# print col from top to bottom.
		for i in range(rowIndex, m):
			print(matrix[i][n-1])
		n -= 1

		# print last row from right to left.
		if(rowIndex < m):
			for i in range(n-1, colIndex-1, -1):
				print(matrix[m-1][i])
			m -= 1
		 
		# print first col from bottom to top.
		if(colIndex < n):
			for i in range(m-1, rowIndex-1, -1):
				print(matrix[i][colIndex])
			colIndex += 1

if __name__ == "__main__":
	matrix = [[0,1,2,3,16],[4,5,6,7,17],[8,9,10,11,18],[12,13,14,15,19],[20,21,22,23,24]]
	#matrix = [[0,1,2,3,16],[4,5,6,7,17]]
	#matrix = [[1,2],[1,2],[1,2]]
	simpleSolution(matrix, 5, 5)