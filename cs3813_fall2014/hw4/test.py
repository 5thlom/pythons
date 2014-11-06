import sys
from time import time
import copy
def matrix_chain_parenthesis(p):
    n=len(p)-1
    s=[[0 for j in range(0,n+1)]for i in range(0,n)]
    for l in range(2,n+1):
        for i in range(1,n-l+2):
            j=i+l-1
            for k in range(i,j):
                    s[i][j]=k
    return s

def matrix_chain_multiply(p,i,j):
    minimum=99999
    if(i==j):
        return 0
    for k in range(i,j):
        count=matrix_chain_multiply(p,i,k)+matrix_chain_multiply(p,k+1,j)+p[i-1]*p[k]*p[j]
        if(count<minimum):
            minimum=count
    return minimum


def optimal_parenthesis(s,i,j):
    if i==j:
        print "A%d"%i,
    else:
        print"(",
        optimal_parenthesis(s,i,s[i][j])
        optimal_parenthesis(s,s[i][j]+1,j)
        print")",
   
def main():
    fin = open("q2.txt", "r")
    p=[]
    for line in fin.readlines():
        for i in line.split(" "):
            p.append(int(i))
    n=len(p)
    count=matrix_chain_multiply(p,1,n-1) 
    s=matrix_chain_parenthesis(p) 
    print "Input: ",p
    print "\ns: "
    for i in range(1,n-1):
        for j in range(1,n):
            print "  %d"%(s[i][j]),
        print ""

    print "\nOptimal Parenthesis :"
    optimal_parenthesis(s,1,n-1)
    print"\n\n Total multiplication is : %d\n" %(count)
main()
