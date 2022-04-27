from collections import deque
def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    
    q = deque()
    for i in range(n):
        if visited[i] == 0:
            q.append(i)
            visited[i] = 1
            answer += 1
        while q:
            now = q.popleft()
            for j in range(n):
                if now != j and computers[now][j] == 1 and visited[j] == 0:
                    q.append(j)
                    visited[j] = 1
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))