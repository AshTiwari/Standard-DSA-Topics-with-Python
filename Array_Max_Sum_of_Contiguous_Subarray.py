# Maximum sum of a contiguous subarray of any length:
from time import time

# step 1: remove left_negative_subarray and right_neg_subarray if any. 
#	  Array now contains left_positive mid_negative (if any) and right_positive
# step 2: cal sum of left_positive_subarray and store as global maximum.
# step 3: add mid_negatve to left_positive. if negative discard it, else continue with it
# step 4: cal sum of right_positive and add to previous sum (if non negative). compare with global maximum.

def pos_neg_pos(array):
	n = len(array)
	leftPositive = 0
	while(leftPositive < n-1 and array[leftPositive] < 0):
		leftPositive += 1
	rightPositive = n-1
	while( rightPositive > 0 and array[rightPositive] < 0):
		rightPositive -= 1 	
	i = leftPositive
	j = rightPositive	
	local_sum = 0
	global_max = 0
	while(i <= j):
		local_sum =local_sum + array[i]		# sum of elements from begininng to current.
		global_max = max(global_max,local_sum)
		k = i+1
		local_negative_sum = 0
		while(k < j and array[k]<0):
			local_negative_sum = local_negative_sum + array[k]
			k = k+1
		if local_sum + local_negative_sum < 0:
			local_sum = 0
		else:
			local_sum = local_sum + local_negative_sum
		i = k		
	return global_max
	 
def kadaneAlgorithm(a):
	size = len(a)
	max_so_far = 0	
	max_ending_here = 0
	for i in range(0, size): 
        	max_ending_here = max_ending_here + a[i] 
        	if max_ending_here < 0: 
            		max_ending_here = 0
          
        	# Do not compare for all elements. Compare only    
        	# when  max_ending_here > 0 
        	elif (max_so_far < max_ending_here): 
            		max_so_far = max_ending_here 
	
	return max_so_far       
    	
def executionTime(function,array):
	start_time = time()
	function(array)
	end_time = time()
	return end_time - start_time
	
if __name__ == "__main__":
	array = [-2,-3,4,-1-2,1,5,-3]

	#print(pos_neg_pos(array))
	#print(kadaneAlgorithm(array))
	print(executionTime(pos_neg_pos,array))
	print(executionTime(kadaneAlgorithm,array))
	