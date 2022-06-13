from sys import stdin

# m가지 보석, n명 - 받지 못하는 학생도 있음, 같은 색의 보석만 가짐


n, m = map(int, stdin.readline().split())
crystals = [0 for i in range(m)]
for i in range(m):
    crystals[i] = int(stdin.readline())

# 보석을 남기지 x
# 보석 종류 <= 학생 수
# 질투심 최소 -> 최대한 모두 비슷하게 나눠 가져야함
# 1 ~ 보석 중 최대 개수로 나누기

# x개로 나눠줬을 때 보석이 남으면 의미 없음
# 남지 않게 나누고, 제일 많이 받은 애가 최소가 되게

max_crystal = max(crystals)

start = 1
end = max_crystal

result = max_crystal

while start <= end:
    mid = (start + end) // 2
    # mid개씩 나눠준다
    
    count = 0 # 총 몇명에게 주었는지
    for crystal in crystals:
        if crystal % mid == 0:
            count = count + crystal // mid
        else:
            count = count + crystal // mid + 1
    if count > n:
        start = mid + 1
    else:
        if result > mid:
            result = mid
        end = mid - 1
print(result)    