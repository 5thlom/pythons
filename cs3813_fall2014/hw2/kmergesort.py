from heapq import*


def kmergesort(lst,k):
	if len(lst)<2:#if length of lst is <2 , we stop
		lst.sort()
		#print lst
		return lst
	
	temp = []
	#print lst
	#print lst
	#using a temp list to save k splitted data and put them into merge function later.
	for i in range(k):
		p = lst[i::k]
		if len(p):#skip empty list
			p=kmergesort(p,k)#for k split, get the returned list and put each lvl of split into a list temp. p is the returned list 
			temp.append(p)
	#print 'temp',temp

	return merge(temp)#after collection of all k split (or same lvl or leafs) we call merge and take the returned result as the ending of current recursive call

	

'''def merge(d):
	heapq.heapify(d)
	b=[]
	for i in range(len(d)):
		b.append(heapq.heappop(d))
	return b


def isEmpty(lis):
	try:
		for a in lis:
			if not isEmpty(a):
				return False
	except:
		return False
	return True

def merge(d,k):
	if d<k:
		d.sort()
		return d
	print "d: ",d
	dv = []
	i=0
	temp=[]
	for i in range(k):
		temp.append(d[i::k])
	index =0


	for i in temp:
		heapq.heappush(dv,(i[0],index))
		index+=1
	print 'here'
	data = heapq.heappop(dv)
	heapq.heappop(temp[data[1]])

	nd = []
	for i in temp:
		nd+=i
	print 'here again'
	print nd
	return data[0]+ merge(nd,k)
'''

def merge(d):
	rv=[]#this to save the return value list
	myheap=[]#this is the k split size heap

	for i in range(len(d)):
		heappush(myheap,(d[i][0],i))#each sublist of d, we push each first element into myheap

	while len(myheap):#when theres still elements in myheap
		data = heappop(myheap)#pop the first one of myheap

		rv.append(data[0])#put the first element into myheap
		heappop(d[data[1]])#pop the elements of the sublist, to ready for the next loop
		if len(d[data[1]]):#if the current sublist still has elements we push an other element into the heap, recording the elements and the index
			heappush(myheap,(d[data[1]][0],data[1]))

	return rv#at the end we have the sorted of all sublist and return it.




print kmergesort([3,1,5,2,4,5,4,3,2,2],5)
#print merge([[4,8],[2,6]])

