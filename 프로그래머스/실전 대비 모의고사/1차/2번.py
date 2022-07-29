def solution(want, number, discount):
    result = 0

    b = {}
    check = {}
    for i in range(len(want)):
        b[want[i]] = number[i]
    
    for i in range(10):
        if discount[i] in check:
            check[discount[i]] += 1
        else:
            check[discount[i]] = 1
    
    front = 0
    end = 9

    while True:
        flag = True
        for key in list(b.keys()):
            if key not in check or check[key] != b[key]:
                flag = False
                break
        if flag:
            result+=1
        
        check[discount[front]] -= 1
        front += 1
        end += 1
        if end == len(discount):
            break
        if discount[end] in check:
            check[discount[end]] += 1
        else:
            check[discount[end]] = 1
    return result