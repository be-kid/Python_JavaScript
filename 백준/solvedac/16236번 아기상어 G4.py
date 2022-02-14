from sys import stdin
from collections import deque

n = int(stdin.readline())
sea = [list(map(int, stdin.readline().split())) for i in range(n)]

shark = 2
count = 0
fish = []
eat = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(x,y):
    global fish
    fish = []
    check = [[True for i in range(n)] for j in range(n)]
    q = deque()

    q.append([0, x, y])
    check[x][y] = False
    while q:
        d, x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and check[nx][ny] and sea[nx][ny]<=shark:
                q.append([d+1, nx, ny])
                check[nx][ny] = False
                if 0< sea[nx][ny] < shark:
                    fish.append([d+1, nx, ny])


x, y = 0, 0
for i in range(n):
    for j in range(n):
        if sea[i][j] == 9:
            x,y = i,j

while True:
    bfs(x,y)
    if len(fish) == 0:
        break
    fish.sort()
    count+=fish[0][0]
    eat+=1
    if eat == shark:
        shark+=1
        eat = 0
    sea[x][y] = 0
    x, y = fish[0][1], fish[0][2]
print(count)
'''
꼭 크기 순으로 먹어야되는건 아니다
먹을 수 있는 모든 물고기 중 가장 가까운 것



아기상어 처음 크기 1, 1초에 상하좌우 한칸씩 이동
자기보다 큰 물고기는 지나갈 수 없다
자기보다 작은 물고기만 먹을 수 있다

먹을 수 있는 물고기가 없을 때 까지 반복
먹을 수 있는 가장 가까운 물고기부터 먹으러 간다
왼쪽위가 우선순위가 높다

자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가

3
0 0 0
0 0 0
0 9 0
0

3
0 0 1
0 0 0
0 9 0
3

4
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4
14

6
5 4 3 2 3 4
4 3 2 3 4 5
3 2 9 5 6 6
2 1 2 3 4 5
3 2 1 6 5 4
6 6 6 6 6 6
60

6
6 0 6 0 6 1
0 0 0 0 0 2
2 3 4 5 6 6
0 0 0 0 0 2
0 2 0 0 0 0
3 9 3 0 0 1
48

6
1 1 1 1 1 1
2 2 6 2 2 3
2 2 5 2 2 3
2 2 2 4 6 3
0 0 0 0 0 6
0 0 0 0 0 9
39
'''