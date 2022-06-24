# 1번
def solution1(size):
    cnt = [0, 0, 0]
    
    for i in size:
        if i == "S":
            cnt[0] += 1
        elif i == "M":
            cnt[1] += 1
        else:
            cnt[2] += 1
    
    return "S"*cnt[0]+"M"*cnt[1]+"L"*cnt[2]

# 2번

# 3번

# ["...X..",
#  "....XX",
#  "..X..."] 
# 6

# ["....X..",
#  "X......",
#  ".....X.",
#  "......."] 
# 15

# ["...X.",
#  ".X..X",
#  "X...X",
#  "..X.."] 
# 9

# ["."] 
# 1


# 4번
from collections import deque
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def solution4(B):
    visited = [[0 for i in range(len(B[0]))] for j in range(len(B))]
    
    dq = deque()
    result = [0, 0, 0]
    for i in range(len(B)):
        for j in range(len(B[0])):
            now = [i, j]
            if B[i][j] == "." or visited[i][j] == 1:
                continue
            dq.append(now)
            
            count = 0
            while dq:
                now = dq.popleft()
                visited[now[0]][now[1]] = 1
                count += 1
                
                for k in range(4):
                    nx = now[0] + dx[k]
                    ny = now[1] + dy[k]
                    if 0 <= nx < len(B) and 0 <= ny < len(B[0]) and B[nx][ny] == "#" and visited[nx][ny] == 0:
                        dq.append([nx, ny])
            
            result[count-1] += 1
    
    return result
    
# B = [".##.#", "#.#..", "#...#", "#.##."]
# [2, 1, 2]

# B = [".#..#", "##..#", "...#."]
# [1, 1, 1]

# B = ["##.", "#.#", ".##"]
# [0, 0, 2]

# B = ["...", "...", "..."]
# [0, 0, 0]

# print(solution4(B))