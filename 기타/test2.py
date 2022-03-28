def solution(instructions):
    result = 0
    
    for com in instructions:
        com = com.split(" ")
        
        if com[0] == "HALT":
            break
        else:
            result = (result + action(com))%360
    return result
            

angle ={"LEFT":270, "RIGHT":90, "TURN":180}

def action(com):
    if len(com) == 1 or com[0] == "TURN":
        return angle[com[0]]
    else:
        if com[0] == "RIGHT":
            return int(com[1])
        else:
            return 360 - int(com[1])
        
        
ex = ["RIGHT"]
ex2 = ["LEFT", "LEFT", "TURN AROUND"]
ex3 = ["LEFT 5", "RIGHT 10", "LEFT 15", "RIGHT 20", "LEFT 25", "RIGHT 30", "LEFT 35", "RIGHT 40"]
ex4 = ["RIGHT 59", "RIGHT", "RIGHT", "HALT", "LEFT", "LEFT", "LEFT"]
ex5 = ["TURN AROUND", "HALT", "LEFT 5", "HALT", "LEFT 5"]
print(solution(ex5))