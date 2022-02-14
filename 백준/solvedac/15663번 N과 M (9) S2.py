from sys import stdin

n, m = map(int, stdin.readline().split())

nums = list(map(int, stdin.readline().split()))
nums.sort()
check = [0 for i in range(n)]
result = set()
def func(k, ans):
    if k == m:
        result.add(ans)
        return
    for i in range(n):
        if check[i] == 0:
            check[i] = 1
            func(k+1, ans+(nums[i],))
            check[i] = 0

func(0, ())


result = sorted(list(result))

for i in result:
    for j in i:
        print(j,end=' ')
    print()