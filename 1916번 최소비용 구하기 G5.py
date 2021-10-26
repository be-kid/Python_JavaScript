from sys import stdin
import heapq
n = int(stdin.readline())
m = int(stdin.readline())
city = {}
for i in range(1, n+1):
   city[i] = {}
for i in range(m):
   s, e, w = map(int, stdin.readline().split())
   if e in city[s]:
      city[s][e] = min(w, city[s][e])
   else:
      city[s][e] = w
s, e = map(int, stdin.readline().split())

inf = float('inf')
d = [inf for i in range(n+1)]
d[s] = 0
h = [(0, s)]

while h:
   now = heapq.heappop(h)
   if d[now[1]] == now[0]:
      for i in city[now[1]]:
         temp = now[0]+city[now[1]][i]
         if d[i] > temp:
            d[i] = temp
            heapq.heappush(h, (temp,i))

print(d[e])
