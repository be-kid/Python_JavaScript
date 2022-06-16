from sys import stdin
import heapq

n = int(stdin.readline())
trees_input = list(map(int, stdin.readline().split()))
h_input = list(map(int, stdin.readline().split()))

t = []
for i in range(n):
    heapq.heappush(t, [h_input[i], trees_input[i]])

answer = 0

for i in range(n):
    tree = heapq.heappop(t)
    answer = answer + tree[1] + i*tree[0]

print(answer)