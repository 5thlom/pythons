# -*- coding: utf-8 -*-
#这个题目 找出 重1到最大的数值 所有可能的path

from collections import defaultdict
'''
#graph = defaultdict(list, {1: [2,3], 2: [5], 3:[2,5], 5:[4]})
graph = defaultdict(list, {1: [2], 2: [3], 3:[2]})

indeg = defaultdict(int)

for u in graph:
    indeg[u]
    for v in graph[u]:
        indeg[v] += 1

queue = []
for u in indeg:
    if indeg[u] == 0:
        queue.append(u)

def tsort(queue, indeg, order):
    if queue == []:
        print order
        return
    
    q2 = queue[:]
    i2 = copy.deepcopy(indeg)
    for i in range(len(q2)):
        u = queue.pop(i)
        for v in graph[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                queue.append(v)
        tsort(queue, indeg, order+[u])
        queue = q2[:]
        indeg = copy.deepcopy(i2)

tsort(queue, indeg, [])

'''




bv = 0
bv2 = 0
def topdown(data,current,target):
    
    if data is None or data[current] is None:
        return 0
    global bv
    for i in data[current]:
        if i is target:
            bv  = bv +1
        topdown(data,i,target)
    return bv

def bottomup(data,current,target):
    #while True:
    global bv2
    currentData = []
    currentData.append(1)
    for i in currentData:
        for j in data[i]:
            #print data[i]
            currentData.append(j)
            if j is target:
                bv2+=1
    return bv2




def checkCYCLIC(data,indeg):
    s = []
    for i in indeg:
        if indeg[i] is 0:
            s.append(i)
    #print s
    while len(s)>0:
        node = s.pop(0)
        for i in data[node]:
            indeg[i]-=1

            if indeg[i]==0:
                s.append(i)
   # print indeg
    counter =0
    for i in indeg:
        counter=+indeg[i]
    #print data,"2"
    if counter==0:
        return True
    else:
        return False


def f():
    with open("q1.txt","r") as read:
        with open("o3.txt","w") as write:
            t = (int)(read.readline())
            #print t

            for i in range(t):
                #print i
                data = {}
                indeg = defaultdict(int)

                v,e = map(int,read.readline().split())
                #print v,e
                b = read.readline().replace('\n\r','').replace('(','').replace(',','').replace(' ','').split(')')[:-1]
                for i in range(v):
                    data[i+1]=[]
                for i in b:
                    n,w = int(i[0]),int(i[1])
                    data[n].append(w)
                for u in data:
                    indeg[u]
                    for v in data[u]:
                        indeg[v] += 1
                
                if checkCYCLIC(data,indeg) == False:
                    print "CYCLIC"
                else:
                    print topdown(data,1,v) #ff is topdown (recursion) solution
                    #print bottomup(data,1,v)
                bv = 0
            #print ff(data,1,5)
                


        write.close()
    read.close()
f()
