import sys
w, h, b = map(int, sys.stdin.readline().split())
result = w*h*b/8/1024/1024
print("%.2f"%result+" MB")

#print(round(h*b*c*s/8/1024/1024, 1), "MB")