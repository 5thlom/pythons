import sys

def f():
	with open("q2.txt", "r") as read:
		with open("q2_o.txt", "w")as write:
			t = (int)(read.readline())
			
			for i in range(t):
				y=[]
				x = read.readline().replace('\n', '').split()
				for i in x:
					x1,y1=map(int,i.split('x'))
					if x1 not in y:
						y.append(x1)
					y.append(y1) 
				#print y
				memo={}

				print topdown(y,1,len(y)-1,memo)
							
		write.close()
	read.close()


def topdown(y,i,j,memo):
	if(i==j):
		return 0
	if (i,j) in memo:
		return memo[i,j]
	else:
		memo[i,j] = sys.maxint
		for k in range(i,j):
			count=topdown(y,i,k,memo)+topdown(y,k+1,j,memo)+y[i-1]*y[k]*y[j]
			if(memo[i,j]>count):
				memo[i,j] = count
		return memo[i,j]


def output2(s,i,j):
    if i==j:
        print "A%d"%i,
    else:
        print"(",
        output2(s,i,s[i][j])
        output2(s,s[i][j]+1,j)
        print")",

def bottomup(p):
	n = len(p)-1
	m = [[0 for j in range(0,n+1)] for i in range(0,n+1)]
	s = [[0 for j in range(0,n+1)] for i in range(0,n)]
	for i in range(1,n+1):
   		m[i][i]=0
   	for l in range(2,n+1):
   		for i in range(1,n-l+2):
   			j = i + l -1
   			m[i][j] = sys.maxint
   			for k in range(i,(j-1)+1):
   				q = m[i][k] + m[k+1][j] + p[i-1] * p[k]*p[j]
   				if q< m[i][j]:
   					m[i][j] = q
   					s[i][j] = k
   	print "here",m[i][j]
	return m,s
'''


def ff(data,i,j,memo):
	if (i==j):
		return 0
	if (i,j) in memo:
		#print (i,j)in memo
		return memo[i,j]
	else:
		#print (i,j)in memo
		memo[i,j] = sys.maxint

		for k in range(i,j):
			t = ff(data,i,k,memo) + ff(data,k+1,j,memo) + data[i][0] * data[k][1] * data[j][1]
			if(memo[i,j]>t):
				memo[i,j] = t
		return memo[i,j]

'''
f()


