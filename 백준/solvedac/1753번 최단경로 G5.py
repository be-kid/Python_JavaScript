from sys import stdin
import heapq

V, E = map(int, stdin.readline().split())
k = int(stdin.readline())

g = {}
for i in range(1, V+1):
    g[i] = {}

for i in range(E):
    u, v, w = map(int, stdin.readline().split())
    if v in g[u]:
        g[u][v] = min(g[u][v], w)
    else:
        g[u][v] = w

inf = float('inf')
table = [inf for i in range(V+1)]
h = []
heapq.heappush(h, [0,k])
table[k] = 0
while h:
    now = heapq.heappop(h)
    if now[0] == table[now[1]]:
        for i in g[now[1]]:
            if table[i] > g[now[1]][i] + table[now[1]]:
                table[i] = g[now[1]][i] + table[now[1]]
                heapq.heappush(h, [table[i], i])

ans = ''
for i in range(1, V+1):
    if table[i] == inf:
        ans+='INF\n'
    else:
        ans+=str(table[i])+'\n'
print(ans)