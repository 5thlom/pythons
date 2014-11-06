# -*- coding: utf-8 -*-
import sys
def lis():
	for line in sys.stdin:
		data = []
		data.append('1a')
		for i in line:
			data.append(i)
		#data=data[:-1]
		data.append('zz')
		track = []
		memo={}
		print data
		opt={}#记录每个字母的最长距离
		back={}#记录每个点的跳跃点
		#print"top_down ", _lis(data,len(data)-1,track,memo)[:-2]
		print bottomup(data,len(data),opt,back)
		print trace(back,data,len(data)-1)[:-2]
		print back



def bottomup(data,j,opt,back):
	opt[0]=0
	for i in range(j):
		maxv = 0
		pt = 0
		for jj in range(i):
			#print "opt[jj",opt[jj]
			#print "asdfa",opt[jj]
			if data[jj] < data[i] and opt[jj] > maxv:#如果当时jj位置得字母比i得字母小 和 当时opt［jj]所记录得max长度 必须要比现在得maxv 长 or maxv必须要比它小 不然就没意义比了
				#print "jj: ",jj,"opt[jj]",opt[jj]
				maxv = opt[jj]#如果如何上面的条件，那就是有可以更新的最大的max长度，maxv＝拿当时所记录的maxv 那就是 现在的maxv有可能是候选者
				#print maxv
				pt = jj#pt记录候选者index，那就是跳点的位置 当时的位置到i位置
		opt[i] = maxv+1#最后拿最大的maxv 就是最大的长度 然后update当时最大的长度到i
		back[i]=pt #update back［i］＝最后的pt 那就是跳跃的地方
	return None
#通过记录点的位置 然后trace出最长的string start在最后一位 因为必然是包括最后一个的。
def trace(back,data,i):
	if i==0:
		return ''#basecase 等于0 就return ‘ ’ 因为不要return index为0的数值 那就是无限小的数值
	else:
		return trace(back,data,back[i]) + data[i]

lis()