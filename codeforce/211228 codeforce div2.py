from sys import stdin 

test = int(stdin.readline())

for t in range(test):
    inf = float('inf')
    
    n = int(stdin.readline())
    arr= [0 for i in range(n+1)]
    nums = []
    for i in range(n):
        l, r = map(int, stdin.readline().split())
        
        for j in range(l, r+1):
            arr[j] += 1
        
        if l == r:
            arr[l] = inf
            nums.append([l, r, l])
        else:
            nums.append([l,r, False])
    
    nums.sort(key = lambda x : x[0]-x[1]+1, reverse=True)
    
    for tmp in nums:
        if tmp[2] == False:
            idx = arr.index(min(arr[tmp[0] : tmp[1]+1]))
            arr[idx] = inf
            print(tmp[0],tmp[1],idx)
        else:
            print(tmp[0],tmp[1],tmp[2])






# problem A
# for t in range(test):
#     n, m, rb, cb, rd, cd = map(int, stdin.readline().split())
#     dr = 1
#     dc = 1
#     count = 0
#     while True:
#         if rb == rd or cb == cd:
#             print(count)
#             break
#         else:
#             if 1 <= rb + dr <= n:
#                 rb = rb + dr
#             else:
#                 dr = dr * -1
#                 rb = rb + dr
            
#             if 1 <= cb + dc <= m:
#                 cb = cb + dc
#             else:
#                 dc = dc * -1
#                 cb = cb + dc        
        
#         count += 1