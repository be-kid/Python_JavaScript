from sys import stdin
from collections import deque

n,m = map(int, stdin.readline().split())
inf = float('inf')
board = [inf for i in range(101)] 
check = [True for i in range(101)]

for i in range(n+m):
    x, y = map(int, stdin.readline().split())
    check[x]=y

q = deque()
q.append(1) #start
board[1] = 0
check[1] = False
while q:
    now = q.popleft()
    
    if now == 100:
        print(board[now])
        break
    for i in range(1, 7):
        next = now+i
        if next<=100 and check[next]==False:
            continue
        elif next<=100 and check[next]==True:
            board[next] = min(board[next], board[now]+1)
            check[next] = False
            q.append(next)
        elif next<=100 and check[next]!=True and check[next]!=False:
            if check[check[next]] == True:
                    board[next]=min(board[next], board[now]+1)
                    board[check[next]] = min(board[check[next]], board[next])
                    q.append(check[next])
                    check[next] = False

'''
주사위 - 1~6
보드 - 1~100
1, 100번 칸은 뱀,사다리 x

3 7
32 62
42 68
12 98
95 13
97 25
93 37
79 27
75 19
49 47
67 17
-> 3

4 9
8 52
6 80
26 42
2 72
51 19
39 11
37 29
81 3
59 5
79 23
53 7
43 33
77 21
-> 5
'''