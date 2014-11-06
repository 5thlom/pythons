import sys
sys.setrecursionlimit(100000)

PRINT = True
MEM = True 

def A(m, n, s="%s", cache={}):
    if PRINT: print s % ("A(%d,%d)" % (m, n)),
    if MEM and (m, n) in cache:
        if PRINT: print "cached: ", cache[m, n]
        return cache[m, n]
    if PRINT: print # new line
    if m == 0:
        cache[m, n] = n + 1
    elif n == 0:
        cache[m, n] = A(m - 1, 1, s)
    else:
        n2 = A(m, n - 1, s % ("A(%d,%%s)" % (m - 1)))
        cache[m, n] = A(m - 1, n2, s)
    return cache[m, n]

m, n = map(int, sys.argv[1:3])
print "A(%d, %d) = %d" % (m, n, A(m, n))