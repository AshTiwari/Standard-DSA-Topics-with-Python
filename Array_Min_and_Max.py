# find min and max in an array


def linearSearch(array):
	minimum = array[0] if len(array) else None 
	maximum = array[0] if len(array) else None
	for i in range(1,len(array)):
		minimum,maximum = min(minimum,array[i]),max(maximum,array[i])
	print(f"Minimum = {minimum}")
	print(f"Maximum = {maximum}")

def tournament(array):
	answer = tournamentRecurssion(array)
	minimum,maximum = answer[0],answer[1]
	print(f"Minimum = {minimum}")
	print(f"Maximum = {maximum}")
def tournamentRecurssion(array):
	if len(array) == 0:
		minimum = maximum = None
	elif len(array) == 1:
		minimum = maximum = array[0]
	else:
		min1,max1 = tournamentRecurssion(array[:len(array)//2])
		min2,max2 = tournamentRecurssion(array[len(array)//2:])
		minimum,maximum = min(min1,min2),max(max1,max2)
	return (minimum,maximum)

def pairwiseComparison(array):
	if len(array) == 0: 
		minimum = maximum = None
		j = 0  
	elif len(array)%2==1: 
		minimum = maximum = array[0]
		j = 1
	elif len(array)%2==0: 
		minimum,maximum = min(array[0],array[1]),max(array[0],array[1]) 
		j = 2
	for i in range(j+1,len(array)-1):
		if array[i]<array[i+1]:
			minimum,maximum = min(minimum,array[i]), max(maximum,array[i+1])	 	
		else:
			minimum,maximum = min(minimum,array[i+1]), max(maximum,array[i])	 
	print(f"Minimum = {minimum}")
	print(f"Maximum = {maximum}")	
	
if __name__ == "__main__":
	oddArray = [4,52,66,64,28,9,44,70,72,1,0]
	evenArray = [4,52,66,64,28,9,44,70,72,1]
	nullArray = []
	singletonArray = [5]

	linearSearch(oddArray)
	linearSearch(evenArray)
	linearSearch(nullArray)
	linearSearch(singletonArray)

	tournament(oddArray)
	tournament(evenArray)
	tournament(nullArray)
	tournament(singletonArray)

	pairwiseComparison(oddArray)
	pairwiseComparison(evenArray)
	pairwiseComparison(nullArray)
	pairwiseComparison(singletonArray)