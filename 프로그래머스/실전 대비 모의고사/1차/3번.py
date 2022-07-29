from collections import deque
def solution(order):
    q = deque()
    s = []
    for i in range(len(order)):
        q.append(i+1)
    
    now = 0
    result = 0
    while q:
        if q[0] == order[now]:
            q.popleft()
            now += 1
            result += 1
        elif len(s) > 0 and s[-1] == order[now]:
            s.pop()
            now += 1
            result += 1
        else:
            s.append(q.popleft())
    
    
    while s:
        if s[-1] == order[now]:
            s.pop()
            result += 1
            now += 1
        else:
            break
    
    return result