def solution(n, horizontal):
    room = [[0 for i in range(n)] for j in range(n)]

    now = [0, 0]
    room[0][0] = 1
    num = 2
    
    def rightAndBottom(cnt, num):    
        for i in range(cnt):
            room[now[0]][now[1]] = num
            num += 1
            now[0] += 1
        now[0] -= 1
        now[1] -= 1
        for i in range(cnt-1):
            room[now[0]][now[1]] = num
            num += 1
            now[1] -= 1
        now[1] += 1
        
        return num

    def bottomAndRight(cnt, num):
        for i in range(cnt):
            room[now[0]][now[1]] = num
            num += 1
            now[1] += 1
        now[1] -= 1
        now[0] -= 1
        for i in range(cnt-1):
            room[now[0]][now[1]] = num
            num += 1
            now[0] -= 1
        now[0] += 1
        
        return num 

    # true면 오른쪽 이동 후 아래로, false면 아래로 이동 후 오른쪽으로
    for i in range(1, n):
        if horizontal:
            now[1] += 1
            num = rightAndBottom(i+1, num)
        else:
            now[0] += 1
            num = bottomAndRight(i+1, num)
        
        horizontal = not horizontal
    
    return room


print(solution(5, False))