from sys import stdin
from collections import deque
import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)

v = int(stdin.readline())
tree = {}

for i in range(1, v+1):
    info = list(map(int, stdin.readline().split()))
    tree[info[0]] = {}
    temp = info[1:-1]
    for j in range(0, len(temp), 2):
        tree[info[0]][temp[j]] = temp[j+1]

start = 1
check = [True for i in range(v+1)]
check[0] = 0
check[start] = 0
def dfs(start):
    for x in tree[start]:
        if check[x]==True:
            check[x] = check[start] + tree[start][x]
            dfs(x)

dfs(start)
start = check.index(max(check))

check = [True for i in range(v+1)]
check[0] = 0
check[start] = 0
dfs(start)

print(max(check))



'''
트리의 지름
임의의 정점에서 가장 먼 정점 x를 찾고
x에서 가장 먼 y를 찾으면 x와 y 사이의 거리가 지름

5
5 4 6 -1
1 3 2 -1
2 4 4 -1
3 1 2 4 3 -1
4 2 4 3 3 5 6 -1
'''