import heapq
from operator import itemgetter


def find(lst,x,k):
	a=[]
	for i, data in enumerate(lst):
		heapq.heappush(a,(abs(data-x),data,i))
	d=[]
	for i in range(k):
		d.append((heapq.heappop(a)[2]))
	#print d
	d.sort()
	rv = []
	#print lst
	#print d
	rv = []
	for i in d:
		rv.append(lst[i])
	return rv
	#	rv+=lst[i]

	#print rv
	#d = sorted(d,key = itemgetter(1,0))
	#return d

#print find([4,1,3,2,7,4], 5.2, 2)
print find([4,1,3,2,7,4], 5.2, 2)
print find([4,1,3,2,7,4], 6.5, 3)

'''
5. Now what if the input array is sorted? Can you do it faster?
   Hint1: you can do O(logn + k) time.
   Hint2: what can you do when you're given a sorted array?

   find([1,2,3,4,4,7], 5.2, 2)	returns   [4,4]
   find([1,2,3,4,4,7], 6.5, 3)	returns   [4,7,4]

   Filename: closest_sorted.py
'''