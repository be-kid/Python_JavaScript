from sys import stdin
from collections import deque

T = int(stdin.readline())
for t in range(T):
    check = [False for i in range(10000)]
    q = deque()
    A, B = map(int, stdin.readline().split())
    q.append(A)
    check[A] = ''
    while q:
        now = q.popleft()
        if now == B:
            print(check[now])
            break

        if check[(now*2)%10000] == False:
            q.append((now*2)%10000)
            check[(now*2)%10000] = check[now]+'D'
        if check[(now-1)%10000] == False:
            q.append((now-1)%10000)
            check[(now-1)%10000] = check[now]+'S'
        temp = int(str(now).zfill(4)[1:]+str(now).zfill(4)[0])
        if check[temp] == False:
            q.append(temp)
            check[temp] = check[now]+'L'
        temp = int(str(now).zfill(4)[-1]+str(now).zfill(4)[:-1])
        if check[temp] == False:
            q.append(temp)
            check[temp] = check[now]+'R'
    
'''
0 1000

1 9

37 5264

0 9998

5000 0

1 1

1 0

-------------------------

SDDLDSLDRDDD
LS
DDRDRDDDDD
SD
D

S
'''