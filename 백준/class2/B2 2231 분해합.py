from re import T
from sys import stdin

n = int(stdin.readline())

num = 1
flag = False
while num < n:
    if n == num + sum(list(map(int, list(str(num))))):
        flag = True
        break
    else:
        num += 1

print(num if flag else 0)