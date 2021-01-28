# merge overlapping interval in the intervals array.

def insertionSort(intervals, n):
	for i in range(1,n):
		j = i
		while(j>0 and intervals[j][0] < intervals[j-1][0]):
			intervals[j], intervals[j-1] = intervals[j-1], intervals[j]
			j -= 1
	return intervals

def simpleMerge(intervals,n):
	i = 0
	while(i < n-1):
		if intervals[i][1] >= intervals[i+1][0]:
			intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
			intervals.remove(intervals[i+1])
			n -= 1 
		else:
			i += 1
	return intervals

def mergeIntervals(intervals):
	# sort the intervals array according to the start value of its interval.
	n = len(intervals)
	intervals = insertionSort(intervals,n)
	intervals = simpleMerge(intervals,n)
	return intervals


if __name__ == "__main__":
	# intervals = [[1,3],[2,4],[6,8],[14,15]]
	# intervals = [[1,4],[0,0]]
	intervals = [[1,4],[3,5],[0,2]]
	print(mergeIntervals(intervals))