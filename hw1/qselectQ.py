def _qselect(index, tree):
    if tree == []:
        print 'h'
        return 0, None

    left, node, right = tree
    num, x = _qselect(index, left)
    if index <= num:
        return num, x
    if index == num+1:
        return num+1, node
    num2, y = _qselect(index - num - 1, right)
    return num+num2+1, y

def qsort(a):
    if a == []: return []
    return [qsort([x for x in a if x < a[0]])] + [a[0]] + \
        [qsort([x for x in a[1:] if x >= a[0]])]
    
tree = qsort([8,5,7,3,4,9])
print tree

#for i in range(5):
print '3', _qselect(3, tree)