from math import ceil
from sys import stdin

n, k = map(int, stdin.readline().split())
mak = [0 for i in range(n)]
for i in range(n):
    mak[i] = int(stdin.readline())

start = 0
end = max(mak)

result = 0
while start <= end:
    mid = ceil((start + end) / 2)
    
    count = 0
    for i in range(n):
        if mid != 0:
            count += mak[i]//mid
    
    if count >= k and result < mid:
        result = mid
    
    if count >= k:
        start = mid + 1
    else:
        end = mid - 1

print(result)