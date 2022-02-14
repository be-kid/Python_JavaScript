from sys import stdin
import heapq

# *2, -1, +1 을 해서 이동한 위치가 q에 들어간다.
# 현재 q에 들어있는 것 중에서 가장 걸리는 시간이 작은 것 부터 우선적으로 처리한다
# 시간 작은 애가 먼저 도착할 확률이 크니까
# 최소 힙을 사용한다 다익스트라

n, k = map(int, stdin.readline().split())
inf = float('inf')
visited = [inf for i in range(100001)]

q = []
heapq.heappush(q, (0, n))
visited[n] = 0

while q:
    cnt, pos = heapq.heappop(q)
    
    move = [(pos, 0), (-1, 1), (1, 1)]

    if visited[pos] == cnt:
        for go, sec in move:
            if 0<=pos+go<=100000 and visited[pos+go] > cnt + sec:
                visited[pos+go] = cnt+sec
                heapq.heappush(q, (cnt+sec, pos+go))

print(visited[k])