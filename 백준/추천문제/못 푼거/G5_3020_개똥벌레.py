from sys import stdin

n, h = map(int, stdin.readline().split())
top = [0 for i in range(h+1)]
bottom = [0 for i in range(h+1)]

for i in range(n//2):
    bottom[int(stdin.readline())]+=1
    top[int(stdin.readline())]+=1
print(top)
print(bottom)

for i in range(1, h+1):
    bottom[i] = bottom[i] + bottom[i-1]
    top[i] = top[i] + top[i-1]
