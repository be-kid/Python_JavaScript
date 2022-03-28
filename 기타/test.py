def solution(stringCode, stringMessage):
    key = {}
    key2 = {}
    num = 1
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in stringCode:
        if len(str(num)) == 1:
            key[i] = '0' + str(num)
            key2['0'+str(num)] = i
        else:
            key[i] = str(num)
            key2[str(num)] = i
        num += 1
        
    ans = ''
    if stringMessage[0] in alpha:
        for i in stringMessage:
            ans+=key[i]
    else:
        for i in range(0, len(stringMessage), 2):
            ans+=key2[stringMessage[i:i+2]]
    
    return ans

print(solution("abcdefghijklmnopqrstuvwxyz", "test"))