from sys import stdin

n, m = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))
check = [0 for i in range(n)]
nums.sort()
def func(k, ans):
    if k == m:
        print(ans)
        return
    
    for i in range(n):
        if check[i]==0:
            check[i]=1
            func(k+1, ans+str(nums[i])+' ')
            check[i]=0




func(0, '')