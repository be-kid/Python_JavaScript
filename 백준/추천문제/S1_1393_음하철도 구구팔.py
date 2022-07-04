from sys import stdin
from math import gcd

xs, ys = map(int, stdin.readline().split())
xe, ye, dx, dy = map(int, stdin.readline().split())

a = gcd(dx, dy)
if a != 0:
    dx = dx // a
    dy = dy // a

def dist(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

result = dist(xe, ye, xs, ys)
while True:
    if dx == 0 and dy == 0:
        break
    xe = xe + dx
    ye = ye + dy
    
    d = dist(xe, ye, xs, ys)
    if d <= result:
        result = d
    else:
        xe = xe - dx
        ye = ye - dy
        break

print(xe, ye)