from sys import stdin

n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))

check = [0 for i in range(n)]
result = [0 for i in range(100000*20 + 1)]
def recur(k, m, p):
    if m == k:
        sum = 0
        for i in range(n):
            if check[i] == 1:
                sum += nums[i]
        result[sum] = 1
        return
    
    for i in range(p, n):
        if check[i] == 0:
            check[i] = 1
            recur(k, m+1, i+1)
            check[i] = 0
            

for i in range(1, n + 1):
    # i개를 골라서 더하기
    recur(i, 0, 0)
    
i = 1
while result[i] == 1:
    i+=1
print(i)