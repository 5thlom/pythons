import sys
def lucky():
	for line in sys.stdin:
		x,y,v=line.split()
		#_luck(x,y,v,len(x)-1,len(y)-1)


def _lucky(x,y,v,i,j):
	if i == -1 or j == -1:
		return ''

def table(s):
	m = len(s)
	pi = [0]*
	
	pi[1]=0
	k=0
	for q in range(2,m):
		while k>0 and s[k+1] != s[q]:
			k = pi[k]
		if s[k+1] == s[q]:
			k = k+1
		pi[q]=k
	return pi

print table("ababaca")



