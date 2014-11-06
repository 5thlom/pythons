import heapq
import sys

def datastream():
	'''k = int(raw_input())
	#print k
	i=0
	a=[]*int(k)
	b=[]
	for line in sys.stdin:
		if(i==k):
			#print 'here'
			break
		heapq.heappush(a,(int(line)*-1))
		i+=1
	print len(line),line
	#for line in sys.stdin:
	#	print line,
		

	

'''
	k = input("")
	a=[]*(k)
	b=[]
	i=0
	while i<k:
		heapq.heappush(a,((int(input("")))*-1))
		i+=1

	j=k
	
	for line in sys.stdin:
		if (a[0]*-1) > int(line):
			heapq.heappop(a)
			heapq.heappush(a,(int(line)*-1))
		
	rv=[i*(-1) for i in a]

	rv.sort()
	return rv
	'''


a = [4
	  ,10
	  ,2
	  ,9
	  ,3
	  ,7
	  ,8
	  ,11
	  ,5
	  ,7
	  ]
'''
print datastream()


