
import sys
from time import time
import copy
def lcs():
	with open("q4.txt","r") as read:
		with open("o4.txt","w") as write:
			for line in read:
				memo={}
				x=' '
				y=' '
				x1,y1 ,z= map(str,line.split())
				x+=x1
				y+=y1
				maxlength = max(len(x),len(y))
				back=[]#[[['',0]]*maxlength]*maxlength#[[('',0)]*maxlength]*maxlength
				print x[1:],y[1:],z
				for i in range(maxlength):
					back.append([])
					for j in range(maxlength):
						back[i].append([('',0)])
				
				result2= bottomUp(x,y,back,z)
					
						
				lv = ''
				for i in back:
					for j in i:
						for z in j:
							if z[1] >= len(z) and len(lv) < z[0]:
								lv = z[0]
				if len(lv)==0:
					print "NO LCS"
				else:
					print lv

		write.close()
 	read.close()


def bottomUp(x,y,back,target):
	#print "here"
	for i in range(1,len(x)):
		for j in range(1,len(y)):
			d=[]
			cur = []
			if x[i] == y[j]:
				for wth in back[i-1][j-1]:
					if wth[1]<len(target) and x[i] == target[wth[1]]:
						d.append((wth[0]+x[i],wth[1]+1))
					else:
						d.append((wth[0]+x[i],wth[1]))
					#for ii in d:
					#	print ii
				back[i][j] = d
			else:
				for blah in back[i-1][j]:
					cur.append((blah[0],blah[1]))
				#for iiii in cur:
				#	print iiii
				for blahx in back[i][j-1]:
					if blahx not in cur:
						cur.append((blahx[0],blahx[1]))
				#for iiiii in cur:
				#	print iiiii
				back[i][j] = cur
					

lcs()
