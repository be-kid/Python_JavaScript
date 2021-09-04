from sys import stdin

n,m = map(int, stdin.readline().split())
tet = [list(map(int,stdin.readline().split())) for i in range(n)]

ans = 0
check = [[0 for i in range(m)] for i in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
def dfs(start, length, blocks):
    global ans
    
    if length == 4:
        ans = max(blocks, ans)
        check[start[0]][start[1]] = 0
        return
    for i in range(4):
        newx = start[0]+dx[i]
        newy = start[1]+dy[i]
        if 0<=newx<n and 0<=newy<m and check[newx][newy] == 0:
            check[start[0]][start[1]] = 1
            dfs((newx,newy),length+1,blocks+tet[newx][newy])
            check[start[0]][start[1]] = 0


for i in range(n):
    for j in range(m):
        check[i][j] = 1
        dfs((i,j), 1, tet[i][j])
        check[i][j] = 0
#ㅗㅜㅏㅓ모양 제외하고 dfs진행

'''
0,0 0,1 0,2 1,1

0,0 0,1 0,2 -1,1

0,0 1,0 2,0 1,1

0,0 1,0 2,0 1,-1

'''
for i in range(n):
    for j in range(m):
        if 0<=i+1<n and 0<=j+2<m:
            ans = max(ans, tet[i][j]+tet[i][j+1]+tet[i][j+2]+tet[i+1][j+1])
        if 0<=i-1<n and 0<=j+2<m:
            ans = max(ans, tet[i][j]+tet[i][j+1]+tet[i][j+2]+tet[i-1][j+1])
        if 0<=i+2<n and 0<=j+1<m:
            ans = max(ans, tet[i][j]+tet[i+1][j]+tet[i+2][j]+tet[i+1][j+1])
        if 0<=i+2<n and 0<=j-1<m:
            ans = max(ans, tet[i][j]+tet[i+1][j]+tet[i+2][j]+tet[i+1][j-1])

print(ans)