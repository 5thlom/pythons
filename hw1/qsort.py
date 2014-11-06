

def sort(a):
  if a==[]:
    return []
  else:
    p = a[0]
    l = [x for x in a if x<p]
    r = [x for x in a[1:] if x >=p]
    return [sort(l)] + [p] + [sort(r)]
                      


def qsort1(list):
  if list == []: 
    return []
  else:
    pivot = list[0]
    lesser = qsort1([x for x in list[1:] if x < pivot])
    greater = qsort1([x for x in list[1:] if x >= pivot])
    return lesser + [pivot] + greater

def sorted(a,m=[]):
  if a==[]:
    return
  else:
    sorted(a[0])
    m.append(a[1])
    sorted(a[2])
  return m

def search(a,x):
  if _search(a,x)==[]:
    return False;
  return True;

def _search(a,x):
  if a==[]:
    return a
  elif a[1]<x:
    return _search(a[2],x)
  elif a[1]>x:
    return _search(a[0],x)
  else:
    return a


def insert(tree,x):
  t = _search(tree,x)
  if t==[]:
    t.extend([[],x,[]])

res=[]
path=[]
depth=[]
def longest(tree):
  x= _longest(tree)
  return x[0],x[2]



def _longest(tree):
  if tree ==[]:
    return [0,0,[],[]]
  else:
    l = _longest(tree[0])
    r = _longest(tree[2])

  if l[0]>=r[0]:
    depth=l[3]+[tree[1]]
  else:
    depth=r[3]+[tree[1]]
  maxdepth = max(l[1],r[1])+1
    #update the current longest depth
  if l[0]>r[0] and l[0]>l[1]+r[1]+1:
    path=l[2] #if leftpath is > the leftdepth + rightDepth + 1 then path is left path
  elif r[0]>l[0] and r[0] > l[1]+r[1]+1:
    path=r[2] #if right path is > the sum or (l+r depth), then r path is the one
  else:
    path=l[3]+[tree[1]]+r[3][::-1]
    #new path is equal left path + right path froom the reverse order
  maxpath = max(l[0],r[0],l[1]+r[1]+1)
  return [maxpath,maxdepth,path,depth]#1,3
    
def Depth(tree):
  return _Depth(tree,depth=[])

def _Depth(tree,depth=[]):
  if tree==[]:
    return [0,[]]
  else:
    l = _Depth(tree[0],depth)
    l = _Depth(tree[2],depth)
  if l[0]>=r[0]:
    depth=l[1]+[tree[1]]
  else:
    depth=r[1]+[tree[1]]
  return [max(l[1],r[1])+1,depth]

def a(tree,path=[]):
  if tree == []:
    return [0,[]]
  else:
    l = getH(tree[0])
    r = getH(tree[2])

    ld = a(tree[0])
    lr = a(tree[2])
    print l,r,ld,lr,tree[1]
    return max(l+r+1,max(lr,ld))

def getH(tree):
  if tree==[]:
    return 0
  return max(getH(tree[0]),getH(tree[2]))+1
#path number, path, heigh, h
