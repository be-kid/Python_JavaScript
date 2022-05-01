from sys import stdin

a, b = map(int, stdin.readline().split())

# x^2 + 2ax + b = 0

x1 = -a + int((a**2 - b)**0.5)
x2 = -a - int((a**2 - b)**0.5)

if x1 > x2:
    print(x2, x1)
elif x1 < x2:
    print(x1, x2)
else:
    print(x1)