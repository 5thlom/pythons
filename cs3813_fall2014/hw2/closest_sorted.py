import bisect
import sys

def find(lst,x,k):
	lst.insert(0,-sys.maxint-1)
	lst.insert(len(lst),sys.maxint)
	pos = bisect.bisect(lst,x)
	lst.insert(pos,x)
	#print lst
	li = pos-1
	ri = pos+1
	d = []
	#print lst[pos]
	for i in range(k):
		if abs(lst[li]-lst[pos])<abs(lst[ri]-lst[pos]):
			d.append(lst[li])
			li = li -1
		else:
			d.append(lst[ri])
			ri = ri+1
	return d




print find([1,2,3,4,4,7], 5.2, 2)	#returns   [4,4]
print find([1,2,3,4,4,7], 6.5, 3)	#returns   [7,4,4]
