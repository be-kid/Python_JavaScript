from sys import path, stdin
from collections import deque

n, k = map(int, stdin.readline().split())

q = deque()
q.append((n, 0))

cnt = 0
inf = float('inf')
min_time = inf
ans = 0
check = [False for i in range(100001)]
check[n] = 0
while q:
    pos, t= q.popleft()
    if pos == k and min_time == inf:
        min_time = t
        ans+=1
    elif pos == k and min_time == t:
        ans+=1
    elif t < min_time:
        if pos+1 <= 100000 and (check[pos+1] == False or check[pos+1] >= t+1):
            q.append((pos+1, t+1))
            check[pos+1] = t+1
        if  pos-1 >= 0 and (check[pos-1] == False or check[pos-1] >= t+1):
            q.append((pos-1, t+1))
            check[pos-1] = t+1
        if pos*2 <= 100000 and (check[pos*2] == False or check[pos*2] >= t+1):
            q.append((pos*2, t+1))
            check[pos*2] = t+1

print(min_time)
print(ans)