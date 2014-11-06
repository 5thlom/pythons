def a(tree):
  if tree == []:
    return 0
  else:
    l = getH(tree[0])
    r = getH(tree[2])

    ld = a(tree[0])
    lr = a(tree[2])
    return max(l+r+1,max(lr,ld))

def getH(tree):
  if tree==[]:
    return 0
  return max(getH(tree[0]),getH(tree[2]))+1