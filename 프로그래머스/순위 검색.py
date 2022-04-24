def solution(info, query):
    answer = []
    for i in range(len(info)):
        info[i] = info[i].split(' ')
    
    for q in query:
        #0 2 4 6 7
        q = q.split(' ')
        q = [q[0], q[2], q[4], q[6], q[7]]
        print(q)
        count = 0
        for i in info:
            flag = True
            for j in range(len(i)-1):
                if q[j] == '-':
                    continue
                if i[j] != q[j]:
                    flag = False
                    break
            if int(i[-1]) < int(q[-1]):
                flag = False
            if flag:
                count+=1
        answer.append(count)
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))