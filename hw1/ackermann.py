from time import time
import sys
sys.setrecursionlimit(10000)

def A(m,n):
	if m==0:
		return n+1
	if m>0 and n==0:
		return A(m-1,1)
	if m>0 and n>0:
		t = A(m, n-1)
		return A(m-1,t)


def A2(m,n,memo={}):
	if (m,n) in memo:
		return memo[m,n]
	else:
		if m>0 and n==0:
			memo[m,n]=A2(m-1,1)
			return memo[m,n]
		if m>0 and n>0:
			memo[m,n]=A2(m-1,A2(m,n-1))
			return memo[m,n]
		if m==0:
			return n+1	



t = time()	
print A(3,2)
print time()-t

t = time()
print A2(3,2)
print time()-t