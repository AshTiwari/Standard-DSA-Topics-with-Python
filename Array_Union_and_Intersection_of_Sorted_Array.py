# Union And Intersection of sorted Array:

def Union(sorted_array_1,sorted_array_2):
	i = 0				# tracks array 1
	j = 0				# tracks array 2
	array = []
	while(i < len(sorted_array_1) and j < len(sorted_array_2)):
		if sorted_array_1[i] < sorted_array_2[j]:
			array.append(sorted_array_1[i])
			i = i+1
		elif sorted_array_1[i] > sorted_array_2[j]:
			array.append(sorted_array_2[j])
			j = j + 1
		elif sorted_array_1[i] == sorted_array_2[j]:
			array.append(sorted_array_1[i])
			i = i+1
			j = j + 1
	if i == len(sorted_array_1) :
		array.extend(sorted_array_2[j:]) 
	elif j == len(sorted_array_2) :
		array.extend(sorted_array_1[i:]) 

	return array

def Intersection(sorted_array_1,sorted_array_2):
	i = 0				# tracks array 1
	j = 0				# tracks array 2
	array = []
	while(i < len(sorted_array_1) and j < len(sorted_array_2)):
		if sorted_array_1[i] == sorted_array_2[j]:
			array.append(sorted_array_1[i])
			i = i+1
			j = j + 1
	
		elif sorted_array_1[i] < sorted_array_2[j]:
			i = i+1
		elif sorted_array_1[i] > sorted_array_2[j]:
			j = j + 1
	return array

if __name__ == "__main__":
	sorted_array_1 = [1,1,3,5,7]
	sorted_array_2 = [0,1,2,4,6,7]
	print(Union(sorted_array_1,sorted_array_2))
	print(Intersection(sorted_array_1,sorted_array_2))