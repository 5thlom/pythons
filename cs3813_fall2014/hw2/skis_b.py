def skis_b():
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