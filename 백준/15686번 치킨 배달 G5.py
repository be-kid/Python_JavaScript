from sys import stdin

def chicken_dist():
    #check를 통해 pick된 치킨집들로 치킨 거리 계산하고 result에 추가
    global check, result, house
    ans = 0
    #각 집에 대해서 선택된 치킨집 중 가장 가까운 거리를 추가
    for home in house:
        #house[home] -> 각 집과 치킨집들과의 거리
        #pick된 치킨집 중에서 제일 가까운거를 선택
        i = 0
        min_dist = float('inf')
        for h in house[home]:
            if check[i] == 1:
                min_dist = min(min_dist, house[home][h])
            i+=1
        ans+=min_dist
    result.append(ans)

def pick_chicken(k, p):
    global check, chicken
    #m개를 다 고르면 치킨거리 계산
    if k == m:
        chicken_dist()
        return
    
    for i in range(p, len(chicken)):
        if check[i] == 0:
            check[i]=1
            pick_chicken(k+1, i+1)
            check[i]=0

#치킨집 최대 13개
#폐업하지 않을 치킨집이 치킨집 수의 절반이상이면 폐업시키면서 찾고
#아니면 살리면서 찾고
#그러면 최악의 경우의 수는 13*12*11*10*9*8
#각 집마다 모든 치킨집에 대한 치킨 거리를 구해놓고
#m개의 치킨집을 골랐을 때 치킨 거리를 구한다
#다 해보고 가장 작은애로 한다

n, m = map(int, stdin.readline().split())
city = [list(map(int, stdin.readline().split())) for i in range(n)]

#모든 치킨집과 집의 위치 저장
chicken = []
house = {}
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house[(i,j)] = {}
        elif city[i][j] == 2:
            chicken.append((i,j))

for x in chicken:
    for h in house:
        house[h][x] = abs(x[0]-h[0]) + abs(x[1]-h[1])

#우선 백트래킹을 사용해서 m개를 고르는 경우로 해결해보자
check = [0 for i in range(len(chicken))]
result = []
pick_chicken(0, 0)

print(min(result))