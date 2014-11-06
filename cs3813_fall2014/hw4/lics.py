# -*- coding: utf-8 -*-

def f():
	with open("q3.txt","r") as read:
		for line in read.readlines():
			x, y = line.split()
			x = ' ' + x 
			y = ' ' + y 
			print x[1:],y[1:]
			rv={}
			maxlength = max(len(x),len(y))
			for i in range(maxlength):#set 最左 和 最上 为空list
				rv[0,i]=[]
				rv[i,0]=[]
			r = ff(x,y,rv)
			lv = ''
			for i in r:
				if len(i) > len(lv):
					lv = i
			if len(lv)==0:
				print "NO LICS\n"
			else:
				print lv
		read.close()



def ff(x,y,rv):
	#rv = {}
	for i in range(1,len(x)):
		for j in range(1,len(y)):
			rv[i,j]=[]
			if x[i] == y[j]:
				rv[i,j].append(x[i])
				for ii in rv[i-1,j-1]:#check 斜线
					#print ii[-1]
					last = ii[-1]
					if last < x[i]:
						rv[i,j].append(ii+x[i])#update 需要更新的string
					else:
						rv[i,j].append(ii)#补充 不需要更新的string
				
			else:

				for iii in rv[i-1,j]:#补充 👆 的数据到rv
					rv[i,j].append(iii)
				for iiii in rv[i,j-1]:#补充 👈 的数据到rv
					rv[i,j].append(iiii)
	#print rv
	return rv[len(x)-1,len(y)-1]




f()
