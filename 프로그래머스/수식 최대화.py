check = [0, 0, 0]
exp = {0:"*", 1:"+", 2:"-"}
answer = 0
def solution(expression):
    prioritize(0, "", expression)
    return answer

def prioritize(n, ex, expression): #연산자 우선순위 정하기
    global answer
    if n == 3:
        result = abs(calculate(ex, expression))
        print("계산결과",result)
        if answer < result:
            answer = result
        return
            
    for i in range(3):
        if check[i] == 0:
            check[i] = 1
            prioritize(n+1, ex+exp[i], expression)
            check[i] = 0
            
def calculate(ex, expression):
    print("식 :",expression)
    if ex == "":
        return int(expression)
    
    splited = expression.split(ex[0])
    result = calculate(ex[1:], splited[0]) 
    for s in splited[1:]:
        if ex[0] == "*":
            result *= calculate(ex[1:], s)
        elif ex[0] == "+":
            result += calculate(ex[1:], s)
        elif ex[0] == "-":
            result -= calculate(ex[1:], s)
    print("중간 계산",result)
    return result
print(solution("100-200*300-500+20"))