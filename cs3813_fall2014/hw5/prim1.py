from heapdict import*
import sys
def f():
	with open("q1.txt","r") as read:
		line = read.readline()
		x,y = line.split()
		

		while(x != '-1' and y != '-1'):
			hd = heapdict()
			line = read.readline().replace('-',' ').replace(':',' ').replace(' ',' ').split()
			data={}
			i = 0
			while i != len(line):
				data[int(line[i]),int(line[i+1])] = int(line[i+2])
				i+=3
			#print line
			print data
			color ={}
			hd[0]=0
			color[0]='b'
			p={}
			for j in range(1,int(x)):
				hd[j]=sys.maxint
				color[j]='w'
			
			ff(hd,data,x,p,color)
			
			if len(p)==int(x)-1:
				print x,
				for i in p:
					print "%s%s%s%s%s" %(p[i],'-',i,':',data[p[i],i]),
			else:
				print "NO SPANNING TREE"
			print ''
			x,y = read.readline().split()





def ff(hd,data,x,p,color):
	#print "start color: ", color
	#cur = 0
	#minv = 999
	#index = 0
	while( len(hd)!=0 ):#if the len of hd is empty, we stop
		v = hd.popitem()#pop the first elm which has two elm,(position, cost)
				
		for keys in data:
		
			if keys[0] == v[0]: #if found the node, then check if the target is used or not
				target = keys[1]
				#print color
				#print color[target]=='w'
				if color[target]=='w' and data[keys[0],target] < hd[target]:#if no cycle and we can update
					hd[target] = data[keys[0],target]#update
					p[target] = keys[0]	#update the possible back pointer
			#end of if statment, if no elm pass the if (check), gona pop another smalest elm and check again.

		#print "v[0]", v[0]
		color[v[0]]='b'#mark the cur elm to be used

		#print len(hd
	




f()
