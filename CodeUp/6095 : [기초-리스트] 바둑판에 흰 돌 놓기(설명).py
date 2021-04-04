# 꼭 다시 풀어보기, 출력 결과물 연습하기 좋음
import sys
n = int(sys.stdin.readline())
a=[]
b=[]
for i in range(n):
  x, y = sys.stdin.readline().split()
  a.append(x)
  b.append(y)
for i in range(n):
  a[i] = int(a[i])
  b[i] = int(b[i])
# print(a)
# print(b)
d=[]
for i in range(20) : 
  d.append([])
  for j in range(20) :  
    d[i].append(0)
# print(d)
for i in range(n):
    d[a[i]][b[i]] = 1
for i in range(1,20):
  for j in range(1,20):
    print(d[i][j], end=' ')
  print()
  # print(d[i])
  # print(d[i])
# print(d)