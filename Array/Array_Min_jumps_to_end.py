# Minimum number of jumps to reach the end.

def numberOfHops(index, n, array, min_jump_dict):
	if min_jump_dict.get(index, None) != None:
		return min_jump_dict[index]
	if array[index] >= (n-1) - index:
		min_jump_dict[index] = 1
	elif array[index] == 0:
		min_jump_dict[index] = -1
	else:
		local_min_hops = -1
		for i in range(array[index],0,-1):
			next_hops = numberOfHops(index+i,n,array,min_jump_dict)
			if next_hops == -1:
				continue
			current_hops = 1 + next_hops 
			local_min_hops = current_hops if local_min_hops == -1 else min(local_min_hops,current_hops)
			
		min_jump_dict[index] = local_min_hops

	return min_jump_dict[index]

def dynamicMethod(array):
	n = len(array)
	min_jump_dict = {n-1:0}

	for j in range(n-1):
		numberOfHops(j, n, array, min_jump_dict)
	return min_jump_dict[0]

def linearSolution(array):
	jump = 0
	current_index = 0
	
	while(current_index < len(array)-1):
		local_max_reach = 0
		for i in range(current_index+1, current_index + array[current_index]+1):
			if i + array[i] >= len(array) - 1:
				next_index = len(array) - 1
				jump += 1 
				break
			if i + array[i] >= local_max_reach:
				next_index = i  
		if current_index == next_index:
			return -1
		current_index = next_index
		jump += 1
		 		
	return jump

if __name__ == "__main__":	
	array = [1, 3, 2, 4, 2, 2, 6, 7, 6, 8, 9]
#	array = [1,0,1]
#	array = [3,1,1,1,1,1,1,1,1,1,1,1,1]
#	array = [1,1,1]
	print(dynamicMethod(array))
	print(linearSolution(array))