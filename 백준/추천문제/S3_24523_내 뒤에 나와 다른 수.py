from sys import stdin
from collections import deque
n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))

# 자기보다 뒤에 있는 숫자 중에서 나와 다른 가장 가까운 수의 위치

q = deque()
result = []

for i in range(n):
    if len(q) == 0 or q[-1] == nums[i]:
        q.append(nums[i])
    else:
        while q:
            q.popleft()
            result.append(i+1)
        q.append(nums[i])

if len(q) > 0:
    for i in range(len(q)):
        result.append(-1)

print(" ".join(list(map(str, result))))
    