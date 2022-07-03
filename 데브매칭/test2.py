def solution(rows, columns, lands):
    land = [[0 for i in range(columns)] for j in range(rows)]

    lake = []

    for l in lands:
        land[l[0]-1][l[1]-1] = 1
    
    visited = [[0 for i in range(columns)] for j in range(rows)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    def dfs(pos, count):
        count += 1
        visited[pos[0]][pos[1]] = 1
        for i in range(4):
            nx = pos[0] + dx[i]
            ny = pos[1] + dy[i]
            if 0 <= nx < rows and 0 <= ny < columns:
                if visited[nx][ny] == 0 and land[nx][ny] == 0:
                    count = dfs([nx, ny], count)
        return count
    # 테두리 바다 제외시키기
    visited[0][0] = 1
    dfs([0, 0], 0)
    
    # 섬 내의 호수 체크
    for i in range(rows):
        for j in range(columns):
            if land[i][j] == 0 and visited[i][j] == 0:
                lake.append(dfs([i, j], 0))

    # 최소값, 최대값
    result = []
    
    if len(lake) == 0:
        lake.append(-1)
    result.append(min(lake))
    result.append(max(lake))

    return result

print(solution(9, 7, [[2,2],[2,3],[2,5],[3,2],[3,4],[3,5],[3,6],[4,3],[4,6],[5,2],[5,5],[6,2],[6,3],[6,4],[6,6],[7,2],[7,6],[8,3],[8,4],[8,5]]))