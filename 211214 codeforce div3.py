from sys import stdin 

test = int(stdin.readline())

#1번
# for t in range(test):
#     nums = list(map(int, stdin.readline().split()))
#     tmp = nums.pop()
#     ans = 0
#     for i in range(0, 4):
#         for j in range(i+1, 5):
#             for k in range(j+1, 6):
#                 if tmp == nums[i]+nums[j]+nums[k]:
#                     print(nums[i],nums[j],nums[k])
#                     break 

#2번
# for t in range(test):
#     n = int(stdin.readline())
#     strings = stdin.readline().rstrip().split()
    
#     ans = strings[0]
    
#     for i in range(1, len(strings)):
#         if ans[-1] == strings[i][0]:
#             ans = ans + strings[i][1:]
#         else:
#             ans = ans + strings[i]
    
#     if len(ans) == n:
#         print(ans)
#     else:
#         print(ans+'a')

