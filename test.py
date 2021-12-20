from sys import stdin 

n = int(stdin.readline())
n+=1
dx = [0,1,0,-1]
dy = [1,0,-1,0]

check = [[0 for i in range(n)] for j in range(n)]

count = 0
def func(pos):
    global count
    if pos[0] == n-1 and pos[1] == n-1:
        count+=1
        return 
    
    for i in range(4):
        nx = pos[0] + dx[i]
        ny = pos[1] + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if check[nx][ny] == 0:
                check[nx][ny] = 1
                func([nx,ny])
                check[nx][ny] = 0
    
check[0][0] = 1    
func([0,0])

print(count)