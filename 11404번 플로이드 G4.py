from sys import stdin

n = int(stdin.readline())
m = int(stdin.readline())

inf = float('inf')
city = [[inf for i in range(n)] for j in range(n)]
for i in range(m):
  a, b, c = map(int, stdin.readline().split())
  if city[a-1][b-1] > c:
    city[a-1][b-1] = c

for k in range(n):
  for i in range(n):
    for j in range(n):
      if i!=j:
        city[i][j] = min(city[i][j], city[i][k]+city[k][j])

for x in city:
  for i in x:
    if i == inf:
      print(0, end=' ')
    else:
      print(i, end=' ')
  print()