from sys import stdin

n = int(stdin.readline())

# 1 1
# 6 2 ~ 7
# 12 8 ~ 19
# 18 20 ~ 37

i = 1
num = 1
while True:
    if num >= n:
        print(i)
        break
    num = num + i * 6
    i += 1