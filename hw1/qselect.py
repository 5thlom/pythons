import random
import sys

def qselect(n,a):
	if len(a)<n:
		return None
	else:
		data = random.randint(0,len(a)-1)
		p = a[data]
		#print data
		#print p
		x = [word for word in a if word<p]
		#just elimiate the current index of data, so avoid multiple data elimiated.
		y = [word for i, word in enumerate(a) if word >=a[data] and i!=data]
		#print x
		#print y
		#print len(x)
		if len(x)+1==n:
			return p
		elif len(x)>n-1:
			return qselect(n,x)
		else:
			return qselect(n-1-len(x),y)


#the qselect shoudl be O(n) because we partition our element each time and only select left or right.
#the worst case should be O(n^2)

def t(index,tree):
	if len(tree)<index:
		return None
	else:
		left=tree
		right = tree
		num= random.randint(0,len(left)-1)
		x=[word for word in left if word<left[num]]

		if index <= num:
			return t(index,x)
		
		if index == num+1:
			return left[num]
		
		num2 = random.randint(0,len(right)-1)
		y=[word for i, word in enumerate(right) if word >=right[num2] and i!=num2]
		return t((index-len(left)-1),right)


