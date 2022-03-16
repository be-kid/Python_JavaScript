def solution(m, n, board):
    # board 90도 돌리기
    # 더이상 부술게 없을 때 까지 탐색
    # 1회 탐색 후 부술 수 있는거 부수기
    board = turn_board(m, n, board)
    flag = True
    while flag:
        flag, board = i_can_break_u(n, m, board)
    answer = 0
    for row in board:
        answer += row.count(0)
    return answer
    
def turn_board(m, n, board):
    new_board = []
    for j in range(n):
        temp = []
        for i in range(m-1, -1, -1):
            temp.append(board[i][j])
        new_board.append(temp)
    return new_board

def i_can_break_u(n, m, board):
    break_point = []
    for i in range(1, n):
        for j in range(1, m):
                if board[i][j] != 0 and board[i][j] == board[i-1][j] and board[i][j] == board[i][j-1] and board[i][j] == board[i-1][j-1]:
                    break_point.append([i,j])
                    break_point.append([i-1, j])
                    break_point.append([i, j-1])
                    break_point.append([i-1, j-1])
    if len(break_point) == 0:
        return False, board
    else:
        for pos in break_point:
            board[pos[0]][pos[1]] = 0
        for i in range(len(board)-1, -1, -1):
            for j in range(len(board[0])-1, -1, -1):
                if board[i][j] == 0:
                    del board[i][j]
                    board[i].append(0)
    
        return True, board

# m = 4
# n = 5
# board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
# answer = 14

m = 6
n = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
# answer = 15
   
print(solution(m, n, board))