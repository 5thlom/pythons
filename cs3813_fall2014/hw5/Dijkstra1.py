
from heapdict import*
import sys
def f():
	with open("q1.txt","r") as read:
		line = read.readline()
		x,y = line.split()
		#print "badfa"

		while(x != '-1' and y != '-1'):
			hd = heapdict()
			line = read.readline().replace('-',' ').replace(':',' ').replace(' ',' ').split()
			data={}
			j = 0
			print line
			while(j != len(line)):
				data[int(line[j]),int(line[j+1])]=int(line[j+2])
				j+=3
			hd[0]=0
			for i in range(1,int(x)):
				hd[i]=sys.maxint
			
			rl = ff(hd,data,x)

			if rl != sys.maxint:
				print rl
			else:
				print "no answer"

			x,y = read.readline().split()
			
			


def ff(hd,data,x):
	while( len(hd)!= 0):
		v = hd.popitem()
		if v[0] == int(x)-1:
			return v[1]
		for keys in data:
			if keys[0] == v[0]:
				target = keys[1]
				hd[target] = min( v[1] + data[keys], hd[target] )
				





f()