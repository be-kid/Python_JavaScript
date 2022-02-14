from sys import stdin
from collections import deque

n, k, a, b = map(int, stdin.readline().split())

#n개의 화분
#초기 k의 수분
#a개에 b만큼 수분
#매일 모든 화분의 수분 1 감소
#수분이 0이 되면 사망

#화분은 n/a일에 한번씩 물은 받는다

q = deque()
for i in range(n//a):
    q.append(k - i)

day = 0
while True:
    if q[0] == 0:
        print(day)
        break
    q.append(q.popleft()+b-n//a)
    day+=1