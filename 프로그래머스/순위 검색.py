def solution(info, query):
    answer = []
    # cpp, java, python
    # backend, frontend
    # junior, senior
    # chicken, pizza
    
    for i in range(len(info)):
        info[i] = info[i].split()
        info[i][-1] = int(info[i][-1])
    
    for i in range(len(query)):
        score = int(query[i].split()[-1])
        query[i] = query[i][0:-len(str(score))-1].split(" and ")
        
        over_score = []
        for j in range(len(info)):
            if info[j][-1] >= score:
                over_score.append(info[j])   
        # 점수가 넘는 애들만 우선 모음
        count = 0
        for over in over_score:
            flag = True 
            for k in range(4):
                if query[i][k] == '-':
                    continue
                elif query[i][k] != over[k]:
                    flag = False
                    break
            if flag:
                count += 1
        answer.append(count)    
    return answer    

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))