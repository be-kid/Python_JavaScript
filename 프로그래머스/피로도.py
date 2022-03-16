check = [0 for i in range(8)]
answer = 0
def solution(k, dungeons):
    combination(0, [], len(dungeons), k, dungeons)  
    return answer  
    
def combination(n, combi, dungeons_len, k, dungeons):
    global answer
    if n == dungeons_len:
        result = calculate(combi, k, dungeons)
        answer = result if answer < result else answer
        return
    
    for i in range(0, dungeons_len):
        if check[i] == 0:
            check[i] = 1
            combination(n+1, combi + [i], dungeons_len, k, dungeons)
            check[i] = 0
            
def calculate(combi, k, dungeons):
    count = 0
    for c in combi:
        if k < dungeons[c][0]:
            break
        else:
            k = k - dungeons[c][1]
            count += 1
    return count


print(solution(80, [[80,20],[50,40],[30,10]]))