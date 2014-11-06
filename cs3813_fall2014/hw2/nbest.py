import random
import time
from operator import itemgetter
import sys
import heapq
sys.setrecursionlimit(1000000)

n=5000
a, b = [random.randint(0,10) for _ in xrange(n)],[random.randint(0,10) for _ in xrange(n)]

n1=4000
a1, b2 = [random.randint(0,10) for _ in xrange(n1)],[random.randint(0,10) for _ in xrange(n1)]

n2=3000
a3, b4 = [random.randint(0,10) for _ in xrange(n2)],[random.randint(0,10) for _ in xrange(n2)]

n3=2000
a5, b6 = [random.randint(0,10) for _ in xrange(n3)],[random.randint(0,10) for _ in xrange(n3)]

n4=1000
a7, b8 = [random.randint(0,10) for _ in xrange(n4)],[random.randint(0,10) for _ in xrange(n4)]



def nbesta(a,b):
	xx = [(x,y,x+y)for x in a for y in b]
	xx = sorted(xx,key=itemgetter(2,1))
	#check x[1] first then x[0][1]
	#x = sorted(li.items(),key=lambda x:(x[1],x[0][1]))
	y=[]
	for i in range(len(a)):
		 y.append((xx[i][0],xx[i][1]))
	return y




def qselect(n,a):
	if a ==[]:
		return None
	else:
		data = random.randint(0,len(a)-1)
		p = a[data][2]
		x = [word for word in a if word[2]<p]
		y = [word for i, word in enumerate(a) if word[2] >=a[data][2]  and i!=data]
		if len(x)+1==n:
			return x+[a[data]]
		elif len(x)>=n:
			return qselect(n,x)
		else:
			return x+[a[data]]+qselect(n-1-len(x),y)
    
'''
def nbestb(a,b):
	a_b = [(x,y,x+y) for x in a for y in b]
	r_v = qselect(len(a),a_b)[:len(a)]
	r_v = sorted(r_v,key = itemgetter(2,1))
	return[(i[0],i[1]) for i in d]
	
'''


def nbestc(a,b):
	a.sort()
	b.sort()
	memo=[]
	myHeap=[]
	memo.append((0,0))
	heapq.heappush(myHeap,(a[0]+b[0],b[0],a[0],0,0))
	c=[]
	d=[]
	
	for i in range((len(a))):
		c=heapq.heappop(myHeap)
		oldy,oldx = c[1],c[2]
		oldyi,oldxi = c[3],c[4] 
		d.append((oldx,oldy))
		if not (oldxi,oldyi+1) in memo:
			memo.append((oldxi,oldyi+1))
			heapq.heappush(myHeap,(a[oldxi]+b[oldyi+1],b[oldyi+1],a[oldxi],oldyi+1,oldxi))
		if not (oldxi+1,oldyi) in memo:
			memo.append((oldxi+1,oldyi))
			heapq.heappush(myHeap,(a[oldxi+1]+b[oldyi],b[oldyi],a[oldxi+1],oldyi,oldxi+1))
			
	return d

t = time.time()
nbesta(a,b)
print 'nbesta : n=5000', time.time()-t


#t = time.time()
#print nbestb(a,b)
#nbestb(a,b)
#print "nbestb: ",time.time()-t



t = time.time()
nbestc(a,b)
print "nbestc: n=5000",time.time()-t



t = time.time()
nbesta(a1,b2)
print 'nbesta : n=4000', time.time()-t


#t = time.time()
#print nbestb(a,b)
#nbestb(a,b)
#print "nbestb: ",time.time()-t



t = time.time()
nbestc(a1,b2)
print "nbestc: n=4000",time.time()-t
t = time.time()
nbesta(a3,b4)
print 'nbesta : n=3000', time.time()-t


#t = time.time()
#print nbestb(a,b)
#nbestb(a,b)
#print "nbestb: ",time.time()-t



t = time.time()
nbestc(a3,b4)
print "nbestc: n=3000",time.time()-t
t = time.time()
nbesta(a5,b6)
print 'nbesta : n=2000', time.time()-t


#t = time.time()
#print nbestb(a,b)
#nbestb(a,b)
#print "nbestb: ",time.time()-t



t = time.time()
nbestc(a5,b6)
print "nbestc: n=2000",time.time()-t
t = time.time()
nbesta(a7,b8)
print 'nbesta : n=1000', time.time()-t


#t = time.time()
#print nbestb(a,b)
#nbestb(a,b)
#print "nbestb: ",time.time()-t



t = time.time()
nbestc(a7,b8)
print "nbestc: n=1000",time.time()-t











