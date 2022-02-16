from sys import stdin

test = int(stdin.readline())

for t in range(test):
    h, w, n = map(int, stdin.readline().split())
    if n % h == 0:
        print(h*100 + n//h)
    else:
        print(n%h*100 + n//h+1)    
    