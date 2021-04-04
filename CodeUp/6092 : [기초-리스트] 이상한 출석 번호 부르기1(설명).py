# 답 안보고 다시 풀어보기
import sys
n = int(sys.stdin.readline())
a = sys.stdin.readline().split()
for i in range(n):
  a[i] = int(a[i])
d = []
for i in range(24):
  d.append(0)
#print(d)
for i in range(n):
  d[a[i]] += 1
for i in range(1, 24):
  print(d[i], end=' ')