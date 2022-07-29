def solution(X, Y):
    x = [0 for i in range(10)]
    y = [0 for i in range(10)]

    for i in X:
        x[int(i)] += 1
    for i in Y:
        y[int(i)] += 1
    
    ans = ''

    for i in range(9, -1, -1):
        while x[i] > 0 and y[i] > 0:
            if ans != '0' or i != 0:            
                ans += str(i)
            x[i] -= 1
            y[i] -= 1
    
    if ans:
        return ans
    return '-1'