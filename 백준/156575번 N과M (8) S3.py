from sys import stdin

n, m = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))

check = [0 for i in range(n)]
nums.sort()

def func(k, s, ans):
    if k == m:
        print(ans)
        return
    
    for i in range(s, n):
        if check[i] < m:
            check[i]+=1
            func(k+1, i, ans+str(nums[i])+' ')
            check[i]-=1


func(0, 0, '')