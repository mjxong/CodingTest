import sys
n = int(sys.stdin.readline())
k = sys.stdin.readline().split()
for i in range(n):
  k[i] = int(k[i])
for i in range(n):
  print(k[n-i-1], end=' ')