import sys
a, m, d, n = map(int, sys.stdin.readline().split())
for i in range(1,n):
  a=a*m
  a+=d
  #a=a*m+d
print(a)