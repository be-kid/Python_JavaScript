from sys import stdin
import sys
limit_number = 10000
sys.setrecursionlimit(limit_number)

# k:체력
n, k = map(int, stdin.readline().split())
attack = list(map(int, stdin.readline().split()))
person = list(map(int, stdin.readline().split()))

ap = []
for i in range(n):
    ap.append([attack[i], person[i]])

ap.sort()

visited = [0 for i in range(n)]
result = 0
def recur(hp, save, p):
    global result
    if hp <= k:
        if result < save:
            result = save

    for i in range(p, n):
        if visited[i] == 0:
            visited[i] = 1
            if hp + hp + ap[i][0] <= k:
                recur(hp + hp + ap[i][0], save + ap[i][1], i + 1)
            visited[i] = 0

recur(0, 0, 0)

print(result)