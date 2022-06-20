from sys import stdin

test = int(stdin.readline())
for t in range(test):
    n = int(stdin.readline())
    rank = []
    for i in range(n):
        x, y = map(int, stdin.readline().split())
        rank.append([x, y])
    
    rank.sort()
    
    s = []
    s.append(rank[0][1])
    for i in range(1, n):
        if s[-1] > rank[i][1]:
            s.append(rank[i][1])
    
    print(len(s))
    