from math import ceil
from sys import stdin

n, m = map(int, stdin.readline().split())
c = [0 for i in range(m)]

for i in range(m):
    c[i] = int(stdin.readline())

jealousy = max(c)
# 보석을 못 받는 학생도 있을 수 있다
# 한 사람은 항상 같은 색의 보석만 갖는다
# 보석을 가장 많이 갖는 학생의 보석이 최소가 되게 한다

# 뭘로 나누어야하지..?
# 보석 종류는 사람수보다 적거나 같다
# 주어진 그대로 배분 -> 제일 많은 보석 수가 답
# 1과 제일 많은 보석 수의 중간값에서 시작 -> 인당 최대 보석 수
# 보석이 남는다 -> 너무 잘게 나눴다 -> start를 mid + 1로 옮김
# 아니다 -> 적당히 나누었다 -> end를 mid - 1로 옮김

start = 1
end = jealousy

while start <= end:
    if (start + end) % 2 == 0:
        mid = (start + end) // 2
    else:
        mid = (start + end) // 2 + 1
    
    count = 0
    for i in range(m):
        count += ceil(c[i]/mid)
    if count <= n:
        if mid < jealousy:
            jealousy = mid
        end = mid - 1
    else:
        start = mid + 1
    
print(jealousy)
'''
5 2
7
4
# 3

7 5
7
1
7
4
4
# 4

'''
