# Union And Intersection of sorted Array:

from sortedArrays import Union
from sortedArrays import Intersection

if __name__ == "__main__":
	sorted_array_1 = [1,1,3,5,7]
	sorted_array_2 = [0,1,1,2,4,6,7]
	print(Union(sorted_array_1,sorted_array_2))
	print(Intersection(sorted_array_1,sorted_array_2))