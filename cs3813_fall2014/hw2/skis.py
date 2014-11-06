from collections import defaultdict

def av():
	n,x = map(int, raw_input().split())
	r = map(int, raw_input().split())
	d = [0]*(x+1)
	for i in range(len(r)):
		d[r[i]]+=1
	rv = 0
	wa = x%2
	for i in range((x+1)/2):
			rv+=min(d[i],d[x-i])
	if wa==0:
		rv+=d[x/2]/2
	return rv

def bv():
	n,x = map(int,raw_input().split())
	r = map(int,raw_input().split())
	d={}
	d = defaultdict(lambda: 0, d)
	for i in range(len(r)):
		d[r[i]]+=1
	rv = 0
	wa = x%2
	for i in range((x+1)/2):
		rv+=min(d[i],d[x-i])
	if wa ==0:
		rv+=d[x/2]/2
	return rv


def cv():
	n,x = map(int, raw_input().split())
	r = map(int,raw_input().split())

	r.sort()

	i=0
	j=len(r)-1
	c=0
	while i<j:
		if r[i]+r[j]==x:
			i+=1
			j-=1
			c+=1
		elif r[i]+r[j]<x:
			i+=1
		elif r[i]+r[j]>x:
			j-=1
	return c


	


print bv()

