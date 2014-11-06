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
  return [maxpath,maxdepth,path,depth]#only need 1 and 3


#longest([[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]])
#the complexity of longest paty should be O(nlgn) because the two recurion call will check all the nodes and reture each recorded data to the parent node