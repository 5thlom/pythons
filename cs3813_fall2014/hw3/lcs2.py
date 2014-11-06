import sys
from time import time
def lcs():
	for line in sys.stdin:
		memo={}
		x=' '
		y=' '
		x1,y1 = map(str,line.split())
		x+=x1
		y+=y1
		maxlength = max(len(x),len(y))
		back = [['']*maxlength]*maxlength
		#result = _lcs(x,y,len(x)-1,len(y)-1,memo)
		#if len(result)==0:
		#	print "no lcs"
		#else:
		#	print result
		result2= bottomUp(x,y,back)
		if len(result2)==0:
			print "no lcs"
		else:
			print result2
		
		
'''
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
'''


def bottomUp(x,y,back):
	for i in range(1,len(x)):
		for j in range(1,len(y)):
			rv1 = ''
			if x[i] == y[j]:
				rv1 = back[i-1][j-1] + x[i]
			rv2 = back[i-1][j]
			rv3 = back[i][j-1]
			back[i][j] = max(rv1,rv2,rv3)
	return back[i-1][j-1]


t = time()
lcs()
print time()-t