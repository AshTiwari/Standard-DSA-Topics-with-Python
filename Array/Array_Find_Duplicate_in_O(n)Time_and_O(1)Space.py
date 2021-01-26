# Return Duplicate elements in an Array with O(n) Time and O(n) Space.
# This code considers all element of array to be positive, however the code can be simply modified for negative numbers.

def updateFunctAndDuplicate(funct,duplicate,x):
	temp = funct
	x = str(x)
	temp = temp.replace('x',x)
	if eval(temp) == 0:
		if x not in duplicate:
			duplicate += ' ' + x 
	else:
		funct = funct + '*(x-' + x + ')'
	return funct,duplicate

def createFunction(array):
	funct = '1'
	duplicate = ''
	for i in array :
		funct,duplicate = updateFunctAndDuplicate(funct,duplicate,i)		
	print(*duplicate.strip())

if __name__ =="__main__":
	array = [1,2,3,1,2,1,5,6,0,0,0]
#	array = [1]
	createFunction(array)

# this code contains 'duplicate' string to store the duplicate numbers.
# it helps in preventing to print the same duplicates twice.
# However, for a really large value of n, this string can be very large.
# Then, we can remove the string but the code will then also print every repetition of duplicate element.