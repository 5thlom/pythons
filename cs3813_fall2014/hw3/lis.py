import sys
def lis():
	for line in sys.stdin:
		data = []
		data.append('1a')
		for i in line:
			data.append(i)
		data=data[:-1]
		data.append('zz')
		track = []
		memo={}
		print data
		opt={}
		back={}
		print _lis(data,len(data)-1,track,memo)[:-2]
		#bottomup(data,len(data),opt,back)
		#print"bottom_up", trace(back,data,len(data)-1)[:-2]



def _lis(it,j,track,memo={}):
	if j==0:
		return ''
	if j in memo:
		return memo[j]
	maxv = 0
	bestTrack = ''
	for i in range(j):
		if it[i] < it[j]:
			rtrack = _lis(it,i,track,memo)+it[j]
			if len(bestTrack) < len(rtrack):
				bestTrack = rtrack
	memo[j]=bestTrack
	return memo[j]


def bottomup(data,j,opt,back):
	opt[0]=0
	for i in range(j):
		maxv = 0
		pt = 0
		for j in range(i):
			if data[j] < data[i] and maxv < opt[j]:
				print maxv
				maxv = opt[j]
				print maxv
				pt = j
			opt[i] = maxv+1
			back[i]=pt
	return opt[i-1]

def trace(back,data,i):
	if i==0:
		return ''
	else:
		return trace(back,data,back[i]) + data[i]
	
lis()