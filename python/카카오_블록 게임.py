from copy import deepcopy
def solution(board):
    cnt = 0
    while True:
        n = len(board)
        group = [False]*(n*n)
        for y in range(n):
            for x in range(n):
                if board[y][x] != 0:
                    if not group[board[y][x]]:
                        group[board[y][x]] = []
                    group[board[y][x]].append((y,x))
        for i in range(n*n):
            if group[i]:
                y1,x1,y2,x2 = 0,0,0,0
                group[i].sort(key=lambda x:x[0])
                y1,y2=group[i][0][0], group[i][-1][0]
                group[i].sort(key=lambda x:x[1])
                x1,x2=group[i][0][1], group[i][-1][1]
                group[i] = [[y1,x1],[y2,x2]]
        for x in range(n):
            for y in range(n):
                if not board[y][x]:
                    board[y][x] = -1
                else:
                    break
        g = []
        for i in range(n*n):
            if group[i]:
                y1,x1,y2,x2 = group[i][0][0],group[i][0][1],group[i][1][0],group[i][1][1]
                found = True
                for y in range(y1,y2+1):
                    for x in range(x1,x2+1):
                        if board[y][x] != i and board[y][x] != -1:
                            found = False
                            break
                    if not found:
                        break
                if found:
                    cnt += 1
                    g.append(i)
        if not g:
            return cnt
        else:
            for idx in g:
                y1,x1,y2,x2 = group[idx][0][0],group[idx][0][1],group[idx][1][0],group[idx][1][1]
                for y in range(y1,y2+1):
                    for x in range(x1,x2+1):
                        board[y][x] = 0
            for y in range(n):
                for x in range(n):
                    if board[y][x] == -1:
                        board[y][x] = 0