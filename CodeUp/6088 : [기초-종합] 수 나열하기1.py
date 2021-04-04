import sys
a, d, n = map(int, sys.stdin.readline().split())
res = a+d*(n-1)
print(res)