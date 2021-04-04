import sys
n = int(sys.stdin.readline())
k = sys.stdin.readline().split()
for i in range(n):
  k[i] = int(k[i])
print(min(k))