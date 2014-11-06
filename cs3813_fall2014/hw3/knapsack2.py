import sys
from collections import defaultdict
import os




def boundedKnapsack():
	n,w = map(int, raw_input().split())
	data = []
	back={}
	memo={}
	for i in range(n):
		data.append(map(int,raw_input().split()))
	print data
	print _boundedknapsack(data,w,n-1,back,memo)
	print track(data,w,n-1,back)
	opt = defaultdict(lambda : defaultdict(lambda : defaultdict(int)))
	back2= defaultdict(lambda : defaultdict(lambda : defaultdict(int)))
	print bup(data,w,n,opt,back2)


def track(data,w,n,back):
	if n==-1:
		return []
	return track(data,w-(back[n,w]*data[n][0]),n-1,back) + [back[n,w]] if (n,w) in back else track(data,w,n-1,back) + [0]



def bup(data,ww,n,opt,back):
	rv_ci =0
	for i in range(n):
		for w in range(0,ww+1):
			maxv = 0
			rv = 0
			rv3 = 0
			for j in range(0,data[i][2]+1):
				if w>= (j*data[i][0]):
					rv = opt[i-1][w-(j*data[i][0])][j] + (j*data[i][1])
				rv3 = opt[i][w][j-1]
				rv1 = opt[i-1][w][j]
				rv = max(rv,rv1,rv3)
					#print rv
				if maxv <= rv:
					maxv = rv
					rv_ci = j
				#print maxv
					opt[i][w][rv_ci] = maxv	
				#print opt[n][w][j]
		
	return opt[i][w][data[i][2]]

boundedKnapsack()


