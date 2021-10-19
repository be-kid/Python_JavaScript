from sys import stdin
from collections import deque

n = int(stdin.readline())
edges = [list(map(int, stdin.readline().split())) for i in range(n-1)]

visited = [0 for i in range(n+1)]

tree = {}
for i in range(1, n+1):
    tree[i] = []

for edge in edges:
    tree[edge[0]].append(edge[1])
    tree[edge[1]].append(edge[0])

q = deque()

q.append(1)
visited[1] = 1

ans = [0 for i in range(n+1)]

while q:
    now = q.popleft()

    for i in tree[now]:
        if visited[i] == 0:
            q.append(i)
            visited[i] = 1
            ans[i] = now

for i in range(2, n+1):
    print(ans[i])