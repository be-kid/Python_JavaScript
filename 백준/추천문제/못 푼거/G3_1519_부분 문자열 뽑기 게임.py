from sys import stdin

n = stdin.readline().rstrip()

# 부분 문자열 구하고
# 원래 수에서 빼고
# 반복
# 내 턴에서 한자리 수를 만들면 승리
# 양의 정수만 고름

len_n = len(n)
def recur(num):
    if len(num) <= 1:
        return 
    
    for i in range(1, len_n): # k자리 수
        for j in range(0, len_n):
            if j+i <= len_n and num[j:j+i][0] != 0:
                recur(str(int(num) - int(num[j:j+i])))
        

recur(n)
# 1234567
# 1, 2, 3, 4, 5, 6, 7
# 12, 23, 34, 45, 56, 67
# 123, 234, 345, 456, 567
# 1234, 2345, 3456, 4567
# 12345, 23456, 34567
# 123456, 234567
