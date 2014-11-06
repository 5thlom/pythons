from heapdict import*
import sys
def f():
	with open("q1.txt","r") as read:
		line = read.readline()
		x,y = line.split()
		

		while(x != '-1' and y != '-1'):
			#hd = heapdict()
			hd = []
			line = read.readline().replace('-',' ').replace(':',' ').replace(' ',' ').split()
			data={}
			j = 0
			while(j != len(line)):
				data[int(line[j]),int(line[j+1])]=int(line[j+2])
				j+=3
				
			hd.append((0,True))
			for i in range(1,int(x)):
				hd.append((sys.maxint,True))
			#print "hd",hd
			print "newLine",data
			#for i in hd:
			#	print i[1]
			rl = ff(hd,data,x)
			print rl

			#if rl != sys.maxint:
			#	print rl
			#else:
			#	print "no answer"

			x,y = read.readline().split()
				


def ff(hd,data,x):

	#flag = False;




	while( ffff(hd)==False ):
		v = fff(hd)
		if (v[0]==0 and v[1]==sys.maxint):#if the poped elm is targe elm and the value is intmax, we know not reachable
			return "No Answer"
		#print v[0],v[1]
		
		#input()
		#hd[v[0]] = -1
		#print hd[v[0]]
		#print v
		#print 'v',v[0]
		if v[0] == int(x)-1:
			#print "here"
			return v[1]
		for keys in data:
			if keys[0] == v[0]:
				target = keys[1]
				
				hd[target] = (min( v[1] + data[ keys[0], target ], hd[target][0] ),True)
		hd[v[0]]=(v[1],False)
									

def ffff(hd):
	
	for i in hd:
		#print type(i)
		if i[1] == True:
			return  False
	return True
	#for i in hd:
	#	print i




def fff(hd):
	minv = sys.maxint
	index = 0
	for i in range(len(hd)):
		if hd[i][0]<minv and hd[i][1]==True:
			minv = hd[i][0]
			index = i
	
	#print hd
	return (index,minv)

f()
