def kmergesort(lst,k):
	if len(lst)<k:
		print lst
		return lst
	size=len(lst)/k
	b = 0
	ss = size
	i=0
	print lst
	while i<k-1:
		left=kmergesort(lst[b:size],k)
		b = size
		size +=ss
		i+=1 
	right=kmergesort(lst[i*ss:len(lst)],k)
	

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

print kmergesort([3,1,5,2,4,5,4,3,2,2,1,1,2,3,32,5],4)