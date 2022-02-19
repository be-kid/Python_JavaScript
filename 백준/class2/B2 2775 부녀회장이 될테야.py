from sys import stdin

test = int(stdin.readline())

apart = [[0 for i in range(15)] for j in range(15)]
for i in range(15):
    apart[0][i] = i
for i in range(1, 15):
    for j in range(1, 15):
        apart[i][j] = apart[i][j-1]+apart[i-1][j]

for t in range(test):
    k = int(stdin.readline())
    n = int(stdin.readline())
    print(apart[k][n])