import sys
a, r, n = map(int, sys.stdin.readline().split())
res = a*r**(n-1)
print(res)

# for i in range(1, n) :
#   a = a*r