from sys import stdin 

test = int(stdin.readline())
# Problem A Fail
# def check2(ans, t):
#     i = 0
#     j = 0
#     while j<len(ans):
#         if ans[j] == t[i]:
#             i+=1
#         else:
#             j+=1

#         if i == 3:
#             return False 
#     return True

# def back(n, len_s, check, ans, s, t):
#     global tmp
#     if n == len_s:
#         if check2(ans, t):
#             tmp = False 
#             return print(ans)
#     elif tmp :
#         for i in range(len_s):
#             if check[i] == 0:
#                 check[i] = 1
#                 back(n+1, len_s, check, ans+s[i], s, t)
#                 check[i] = 0

# for t in range(test):
#     s = list(stdin.readline().rstrip())
#     t = stdin.readline().rstrip()
    
#     s.sort()
    
#     check = [0 for i in range(len(s))]
#     tmp = True
#     back(0, len(s), check, '', s, t)


# Problem B
# def gcd(a, b):
#     if a < b:
#         a, b = b, a 
        
#     if b == 0:
#         return a 
    
#     return gcd(b, a%b)

# for t in range(test):
#     n = int(stdin.readline())
    
#     n -= 1
    
#     for i in range(2, n//2 + 1):
#         if gcd(i, n-i) == 1:
#             print(i, n-i, 1)
#             break