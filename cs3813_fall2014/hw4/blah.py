
'''
import sys
from time import time
def lcs():
	for line in sys.stdin:
		memo={}
		x=' '
		y=' '
		x1,y1 ,z= map(str,line.split())
		x+=x1
		y+=y1
		maxlength = max(len(x),len(y))
		back=[]#[[['',0]]*maxlength]*maxlength#[[('',0)]*maxlength]*maxlength
		print x,y,z
		for i in range(maxlength):
			back.append([])
			for j in range(maxlength):
				back[i].append(['',0])
		#print back
		#result = _lcs(x,y,len(x)-1,len(y)-1,memo)
		#if len(result)==0:
		#	print "no lcs"
		#else:
		#	print result
		
		result2= bottomUp(x,y,back,z)
		if len(result2)==0:
			print "no lcs"
		else:
			print result2
		for i in back:
			print i
		
		

def _lcs(x,y,i,j,memo):
	if i == 0 or j == 0:
		return ''
	if (i,j) in memo:
		return memo[i,j]
	else:
		rv1 =''
		if x[i] == y[j]:
			rv1 = _lcs(x,y,i-1,j-1,memo)+x[i]
		rv2 = _lcs(x,y,i-1,j,memo)
		rv3 = _lcs(x,y,i,j-1,memo)
		#print rv1,rv2,rv3
		memo[i,j] = max(rv1,rv2,rv3)
		return memo[i,j]



def bottomUp(x,y,back,target):
	for i in range(1,len(x)):
		for j in range(1,len(y)):
			rv1 = ''
			if x[i] == y[j]:
				rv1 = back[i-1][j-1][0] + x[i]
				if back[i-1][j-1][1]<len(target) and x[i]==target[back[i-1][j-1][1]]:
					#print "Here"
					back[i][j][1] = back[i-1][j-1][1] + 1
				else:
					back[i][j][1] = back[i-1][j-1][1]
			rv2 = back[i-1][j][0]
			rv3 = back[i][j-1][0]

			s = ''
			blah = 0
			if len(rv1)>len(rv2):
				s = rv1
				blah = back[i][j][1]
			else:
				s = rv2
				blah = back[i-1][j][1]
			if len(s)<len(rv3):
				s = rv3
				blah = back[i][j-1][1]
			back[i][j][0] = s
			back[i][j][1] = blah
			#print i,j,s
	return back[i][j][0]


#t = time()
lcs()
#print time()-t

'''

