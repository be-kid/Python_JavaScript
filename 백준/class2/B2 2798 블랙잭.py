from sys import stdin

n, m = map(int, stdin.readline().split())
cards = list(map(int, stdin.readline().split()))

result = 0
for i in range(0, n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if result < cards[i]+cards[j]+cards[k] <= m:
                result = cards[i]+cards[j]+cards[k]

print(result)

'''
result = 0
check = [0 for i in range(n)]
def black(k, total, p):
    global result
    if k == 3:
        if result < total <= m:
            result = total
            return
    
    for i in range(p, n):
        if check[i] == 0:
            check[i] = 1
            black(k+1, total+cards[i], i+1)
            check[i] = 0

black(0, 0, 0)
print(result)
'''