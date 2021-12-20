from sys import stdin 

test = int(stdin.readline())

for t in range(test):
    a, result = map(str, stdin.readline().split())
    b = ''
    state = True
    while True:
        tmp1 = int(result[-1])
        tmp2 = int(a[-1])
        result = result[:-1]
        if len(a) == 1:
            a = '0'
        else:
            a = a[:-1]
        
        if tmp1 >= tmp2:
            b = str(tmp1 - tmp2) + b 
        else:
            tmp1 = (int(result[-1]))*10 + int(tmp1)
            result = result[:-1]
            if tmp1 > 18:
                state = False 
                break 
            elif tmp1 - tmp2 < 0:
                state = False
                break
            else:
                b = str(tmp1 - tmp2) + b 
        
        if result == '':
            break
    
    if state:
        if a != '0':
            print(-1)
        else:
            print(int(b))
    else:
        print(-1)

# B problem
# nums = set([1])
# i = 2
# while True:
#     if i*i <= 1000000000:
#         nums.add(i*i)
#     if i*i*i <= 1000000000:
#         nums.add(i*i*i)
        
#     if i*i>1000000000 and i*i*i>1000000000:
#         break 
#     i+=1

# nums = list(nums)
# nums.sort()

# for t in range(test):
#     n = int(stdin.readline())
    
#     cnt = 0
#     for i in nums:
#         if i<=n:
#             cnt+=1
#         else:
#             break 
    
#     print(cnt)

# A problem
# for t in range(test):
#     s = stdin.readline().rstrip()
    
#     if len(s)%2==1:
#         print("NO")
#     else:
#         if s[:len(s)//2] == s[len(s)//2:]:
#             print("YES")
#         else:
#             print("NO")

