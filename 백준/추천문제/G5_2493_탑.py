from sys import stdin
from collections import deque

n = int(stdin.readline())
towers = list(map(int, stdin.readline().split()))

s = deque()
s.append([100000001, 0])

# stack -> [높이, idx]
# 스택에 들어갈 때 자기보다 낮은거를 꺼냄
# 빠져나갈 때 기록, 자기 앞에 있는 것의 idx

answer = [0 for i in range(n+1)]

for i in range(n):
    tower = towers[i]
    while tower > s[-1][0]:
        top = s.pop()
        answer[top[1]] = s[-1][1]
    s.append([tower, i+1])

while len(s) > 1:
    top = s.pop()
    answer[top[1]] = s[-1][1]

result = ''
for i in range(1, n + 1):
    result += str(answer[i])+' '
    
print(result)