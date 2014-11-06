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
				
				hd[int(line[j]),int(line[j+1])] = int(line[j+2])
				j+=3
			print data
			color = []

			#assign color to each v
			for i in range(int(x)):
				color.append(i)

			ff(data,hd,color)
			x,y = read.readline().split()



def ff(data,hd,color):
	#e = hd.popitem()

	result = []
	while(True):
		#pick the possible smallest edge
		e = hd.popitem()
		u = e[0][0]
		v = e[0][1]
		cost = e[1]
		print "Current smallest Edge",e,"u",u,"v",v,"cost",cost
		break
		#check if the current picked edge will make a cycle
		



f()