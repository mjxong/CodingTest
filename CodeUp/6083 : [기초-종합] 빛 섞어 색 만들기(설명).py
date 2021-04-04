# 시간 초과에 대해서 공부
import sys
r, g, b = map(int, sys.stdin.readline().split())
for i in range(r):
  for j in range(g):
    for k in range(b):
      print('{} {} {}'.format(i, j, k))
print(r*g*b)