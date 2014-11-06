import sys
sys.setrecursionlimit(100000)
def mergesort(lt,s):
	if len(lt)<s:
		#print 'here'
		return lt
	size = len(lt)/s
	ss = size
	begin = 0
	i =0
	while i < s-1:
		l=mergesort(lt[begin:size],s)
		#print l
		begin = size
		size +=ss
		#print size
		i+=1
		#print i,size
		#print i
	#x = raw_input()
	f = (i)*ss
	r=mergesort(lt[f:len(lt)],s)
	#return merge(l,r)
	print l,r

def merge(left,right):
	if not len(left) or not len(right):
		return left or right
	else:
		if left[0]<right[0]:
			y =  [left[0]]+merge(left[1:],right)
			#print y
			return y
		y= [right[0]]+merge(left,right[1:])
		#print y
		return y


print mergesort([3,1,5,2,4,5],2)
