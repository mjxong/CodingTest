import sys
li=[]
for i in range(19):
  li.append([])
  z = input().split()
  for j in z:
    li[i].append(int(j))
# print(li)
n = int(input())
x = []
y = []
for i in range(n):
  a, b = map(int, input().split())
  for j in range(19):
    li[a-1][j] = 1 if li[a-1][j] != 1 else 0
    li[j][b-1] = 1 if li[j][b-1] != 1 else 0
for i in li:
  print(' '.join(map(str, i)))