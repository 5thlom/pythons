import sys
from collections import defaultdict
import os
'''
opt = defaultdict(lambda : defaultdict(int))
memo ={}

def knapsack():
	n,w = map(int, raw_input().split())
	dataset = []
	track = [0]*n
	memo = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))	
	for i,line in enumerate(sys.stdin):
		wi,vi,ci = line.split()
		dataset.append((int(wi),int(vi),int(ci)))
	print dataset
	x,y=_knapsack(n,dataset[n-1][2],n-1,w,dataset,track,memo)
	print x
	print y


def knapsackII():
	n,w = map(int,raw_input().split())
	ws = [0]
	vi = [0]
	ci = []
	for line in sys.stdin:
		x,y,z = line.split()
		ws.append(int(x))
		vi.append(int(y))
		for i in range(int(z)-1):
			ws.append(int(x))
			vi.append(int(y))
	print bottomup(len(ws)-1,w,ws,vi)#_knapsackII(w,len(vi),ws,vi)

		

#dataset[#0 = wi, #1 = vi, #2 = ci]
# 0 = weight of item
# 1 = value of item
# 2 = copy of item


def _knapsack(s,j,n,w,dataset,track,memo):
	#if (w,n,j) in memo:
		#print memo[w,dataset[n][1],j][0],memo[w,dataset[n][1],j][1]
	#	return memo[w,n,j][0],memo[w,n,j][1]
	if w==0 or n<0:
		#memo[j,n,w] =(0,[0]*s)
		memo[w,n,j]=(0,[0]*s)
		return memo[w,n,j]
	
	xtrack=[0]*s
	x=0
	if dataset[n][0]<=w and j>0:
		x , xtrack = _knapsack(s, j-1, n, w-dataset[n][0], dataset, track,memo)
		x = x + dataset[n][1]
		
	y , ytrack = _knapsack(s, dataset[n-1][2], n-1, w, dataset, track,memo)
	if max(x,y) == x:
		xtrack[n] = xtrack[n]+1
		memo[w,n,j]=(x,xtrack)
						#print j,n,w,'-->',memo[j,n,w],'x wins'
		#print memo[n][w][j][0],memo[n][w][j][1]
		return memo[w,n,j][0],memo[w,n,j][1]
	else:
		memo[w,n,j]=(y,ytrack)
				#print j,n,w,'-->',memo[j,n,w],'y wins'
		#print memo[n][w][j][0],memo[n][w][j][1]
		return memo[w,n,j][0],memo[w,n,j][1]

def _knapsackII(maxv,n,ws=[],vs=[]):
	track =[0,0,0]
	print maxv, n, ws, vs
	for w in range(1,maxv+1):
		for i in range(1, n):
			if w>=ws[i] and output[i-1][w-ws[i]]+vs[i]>output[i][w]:
				output[i][w]=output[i-1][w-ws[i]]+vs[i]
			else:
				output[i][w] = output[i-1,w]
			print 'here'
	return output[i][w]





def bottomup(n, W,ws,vs):    
    for w in range(1, W+1):
        for i in range(1, n+1):
            t1 = opt[i-1][w]
            t2 = opt[i-1][w-ws[i]] + vs[i] if w >= ws[i] else -1000
            if t2 > t1:
                opt[i][w] = t2
                #back[i][w] = True
            else:
                opt[i][w] = t1
                #back[i][w] = False
    return ont[w][j]


'''

def boundedKnapsack():
	n,w = map(int, raw_input().split())
	data = []
	back={}
	memo={}
	for i in range(n):
		data.append(map(int,raw_input().split()))
    
	print data
	print back
	print _boundedknapsack(data,w,n-1,back,memo)
    
	print back
	print track(data,w,n-1,back)
	#print "non-zero cells:", sum(len(d) for d in memo.values())
	

	#wi = data[n][0]
	#vi = data[n][1]

def _boundedknapsack(data,w,n,back,memo={}):
	if w == 0 or n ==-1:
		return 0
	if (n, w) in memo:
		return memo[n,w]
	else:
		ci = data[n][2]
		maxv = 0
		rv_ci = 0
		rv = 0
		while ci >= 0 :
			if  w >= ci*data[n][0]:
				rv = _boundedknapsack(data,w-(ci*data[n][0]),n-1,back) + (ci*data[n][1]) 
			if  maxv < rv:
				maxv = rv
				rv_ci = ci
			ci-=1
		memo[n, w] = maxv
		back[n,w] = rv_ci
		return memo[n, w]



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






	
#knapsack()
#knapsackII()