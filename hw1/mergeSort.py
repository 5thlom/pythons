def mergesort(l):
	if len(l) < 2:
		return l
 	left,right = mergesort(l[:len(l)/2]),mergesort(l[len(l)/2:])
	#right = mergesort(list[len(list)/2:])
	#print left,right
	#print 'left: ' , left
	#print 'right: ', right
	#a=raw_input()
	x =merge(left,right)
	#print 'x',x
	return x

def merge(left,right):
	#print'mergeB ',left ,right
	#a=raw_input()
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


print mergesort([3,1,5,2,4])