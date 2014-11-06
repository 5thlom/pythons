import sys
def lcs():
	for line in sys.stdin:
		memo={}
		x,y = map(str,line.split())
		back = [[0]*(len(x)+1)]*(len(y)+1)
		result = _lcs(x,y,len(x)-1,len(y)-1,memo)
		print x,y
		print result
		#print bottomUp(x,y,back={})

def _lcs(x,y,i,j,memo):
	if i == -1 or j == -1:
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



def bottomUp(x,y,back):
	for i in range(1,len(x)+1):
		for j in range(len(y)+1):
			rv1 = 0
			if x[i] == y[j]:
				rv1 = back[i-1,j-1] + x[i]
			rv2 = back[i-1,j]
			rv3 = back[i,j-1]
			back[i,j] = max(len(rv1),len(rv2),rv3)
	return back[i,j]



lcs()