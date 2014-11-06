def skis_a():
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