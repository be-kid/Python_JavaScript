from sys import stdin

n = int(stdin.readline())

check = [0 for i in range(n+1)]
pnum = []
i = 2
# check[x] = 1 이면 소수, 2면 아님
while i <= n:
    if check[i] == 0:
        check[i] = 1
        pnum.append(i)
    
    for j in range(i*2, n+1, i):
        check[j] = 2
    
    i+=1

flag = True
if len(pnum) == 0:
    flag = False

s = 0
e = 0

pnumLen = len(pnum)
if flag:
    total = pnum[0]
result = 0
while flag and s <= e:
    if total == n:
        result += 1
        if e + 1 < pnumLen:
            e += 1
        total += pnum[e]
        
    elif total < n:
        if e + 1 < pnumLen:
            e += 1
        total += pnum[e]
    
    elif total > n:
        total -= pnum[s]
        s += 1
        
print(result)