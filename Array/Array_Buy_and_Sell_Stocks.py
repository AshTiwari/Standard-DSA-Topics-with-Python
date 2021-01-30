# Best time to buy and sell stocks.

def nestedLoop(array):
	#number_of_iterations = 0
	buy = sell = -1
	max_profit = -1
	n = len(array)
	for i in range(n):
		for j in range(i+1,n):
			#number_of_iterations += 1
			if array[j]-array[i] > max_profit:
				max_profit = array[j]-array[i]
				buy, sell = i, j
	print(number_of_iterations)
	return max_profit

def newLogic(array):
	number_of_iterations = 0
	buy = sell = -1
	max_profit = -1
	n = len(array)
	max_profit_index = n-1
	max_price = array[max_profit_index]	
	
	for i in range(n-2,-1,-1):
		number_of_iterations += 1
		if max_price - array[i] > max_profit:
			buy = i
			sell = max_profit_index
			max_profit = max_price - array[i]
		
		if array[i] > max_price:	
			max_price = array[i]
			max_profit_index = i
	print(number_of_iterations)
	return max_profit

if __name__ == "__main__":
	array = [7,1,4,5,6,3]
	print(nestedLoop(array))
	print(newLogic(array))