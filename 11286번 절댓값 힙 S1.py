from sys import stdin
import heapq

n = int(stdin.readline())

h = []
for i in range(n):
  com = int(stdin.readline())

  if com == 0:
    if h:
      temp = heapq.heappop(h)
      print(temp[0]*temp[1])
    else:
      print(0)
  else:
    if com > 0:
      heapq.heappush(h, (com, 1))
    else:
      heapq.heappush(h, (-com, -1))
