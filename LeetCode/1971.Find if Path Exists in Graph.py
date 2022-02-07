from collections import deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = {}
        for i in range(n):
            g[i] = []
        for edge in edges:
            g[edge[0]].append(edge[1])
            g[edge[1]].append(edge[0])
            
#  dfs 반복문
#         s = deque()
#         s.append(source)
        
#         visited = [0 for i in range(n)]
        
#         while s:
#             now = s.pop()
            
#             if now == destination:
#                 return True
            
#             visited[now] = 1
#             for pos in g[now]:
#                 if visited[pos] == 0:
#                     s.append(pos)
                    
#         return False

#. dfs 재귀
#         visited = [0 for i in range(n)]
    
#         def dfs(currentPos):
#             if currentPos == destination:
#                 return True

#             visited[currentPos] = 1

#             for pos in g[currentPos]:
#                 if visited[pos] == 0:
#                     if dfs(pos):
#                         return True
#             return False

#         return dfs(source)    


#  bfs
        q = deque()
        q.append(source)
        visited = [0 for i in range(n)]
        
        while q:
            now = q.popleft()
            
            if now == destination:
                return True
            
            visited[now] = 1
            for pos in g[now]:
                if visited[pos] == 0:
                    q.append(pos)
                    
        return False
    
    
    
    