from sys import stdin

n = int(stdin.readline())
cur_state = list(stdin.readline().rstrip())
result_state = stdin.readline().rstrip()

def change(flag, state):
    if flag == 0:
        state[0] = "0" if state[0] == "1" else "1"
        state[1] = "0" if state[1] == "1" else "1"
    
        count = 1
    else:
        count = 0
    for i in range(1, n):
        if state[i-1] == result_state[i-1]:
            continue
        else:
            if i != n-1:
                state[i-1] = "0" if state[i-1] == "1" else "1"
                state[i] = "0" if state[i] == "1" else "1"
                state[i+1] = "0" if state[i+1] == "1" else "1"
            else:
                state[i-1] = "0" if state[i-1] == "1" else "1"
                state[i] = "0" if state[i] == "1" else "1"
            count += 1
    if "".join(state) == result_state:
        return count
    else:
        return -1

first = change(0, cur_state[:])
second = change(1, cur_state[:])

if first != -1 and second != -1:
    print(min(first, second))
elif first == -1 and second == -1:
    print(-1)
else:
    print(max(first, second))