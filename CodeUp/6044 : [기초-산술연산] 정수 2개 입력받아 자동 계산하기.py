a, b = map(int, input().split())
c = a/b
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
# print('%.2f'%c) => 정화도 출력이므로 출력 서식지정자가 아닌 round
print(round(a/b,2))
# import sys

# def num_sum(n1, n2):
#     return n1 + n2

# def num_minus(n1, n2):
#     return n1 - n2

# def num_mul(n1, n2):
#     return n1 * n2

# def num_mok(n1, n2):
#     return n1 // n2

# def num_nameoji(n1, n2):
#     return n1 % n2

# def num_nanun_gab(n1, n2):
#     return round(n1/n2, 2)

# num1, num2 = map(int,sys.stdin.readline().split())


# print(num_sum(num1, num2))
# print(num_minus(num1, num2))
# print(num_mul(num1, num2))
# print(num_mok(num1, num2))
# print(num_nameoji(num1, num2))
# print(num_nanun_gab(num1, num2))