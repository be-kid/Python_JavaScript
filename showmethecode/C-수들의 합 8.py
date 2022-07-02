from sys import stdin 

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
b = list(map(int, stdin.readline().split()))

pa = [0]
pb = [0]

for i in range(n):
    pa.append(pa[-1] + a[i])
    pb.append(pb[-1] + b[i])

count = 0
for i in range(1, n+1):
    for j in range(i, n+1):
        if i == j:
            if a[i-1] == b[j-1]:
                count += 1
        else:
            if pa[j] - pa[i-1] == pb[j] - pb[i-1]:
                count += 1
                

print(count)