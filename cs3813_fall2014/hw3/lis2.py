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
		#print data
		opt={}
		back={}
		#print"top_down ", _lis(data,len(data)-1,track,memo)[:-2]
		bottomup(data,len(data),opt,back)
		print"bottom_up", trace(back,data,len(data)-1)[:-2]



def bottomup(data,j,opt,back):
	opt[0]=0
	for i in range(j):
		maxv = 0
		pt = 0
		for j in range(i):
			if data[j] < data[i] and maxv < opt[j]:
				maxv = opt[j]
				pt = j
			opt[i] = maxv+1
			back[i]=pt
			print opt[i]
	return opt[i-1]

def trace(back,data,i):
	if i==0:
		return ''
	else:
		return trace(back,data,back[i]) + data[i]

lis()