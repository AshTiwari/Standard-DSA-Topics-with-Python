# Return Duplicate elements in an Array with O(n) Time and O(n) Space.

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