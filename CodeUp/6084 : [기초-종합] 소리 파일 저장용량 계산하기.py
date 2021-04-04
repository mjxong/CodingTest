# 정확도가 "%.1f"%~인지 round함수인지 확인
import sys
h, b, c, s = map(int, sys.stdin.readline().split())
result = h*b*c*s/8/1024/1024
print("%.1f"%result+" MB")

#print(round(h*b*c*s/8/1024/1024, 1), "MB")