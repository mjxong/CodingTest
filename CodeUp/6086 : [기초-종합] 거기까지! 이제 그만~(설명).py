import sys
n = int(sys.stdin.readline())
res = 0
for i in range(1,n+1):
  res += i
  if res >= n:
    break
print(res)

# while True:
#   res=res+a
#   a=a+1
#   if res >= n:
#     break