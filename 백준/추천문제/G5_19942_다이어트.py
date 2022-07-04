from sys import stdin

n = int(stdin.readline())
mp, mf, ms, mv = map(int, stdin.readline().split())
ingredients = [list(map(int, stdin.readline().split())) for i in range(n)]

check = [0 for i in range(n)]

min_price = float('inf')
result = ""
def recur(p, np, nf, ns, nv, price, pick):
    global min_price, result
    if np>=mp and nf>=mf and ns>=ms and nv>=mv:
        if min_price > price:
            min_price = price
            result = pick
    
    for i in range(p, n):
        if check[i] == 0:
            check[i] = 1
            recur(i + 1, np+ingredients[i][0], nf+ingredients[i][1], ns+ingredients[i][2], nv+ingredients[i][3], price+ingredients[i][4], pick+str(i+1)+" ")
            check[i] = 0
            
recur(0, 0, 0, 0, 0, 0, "")

if min_price == float('inf'):
    print(-1)
else:
    print(min_price)
    print(result)