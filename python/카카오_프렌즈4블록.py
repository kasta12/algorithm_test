"""
O(NMNM)
최악의 경우 20만번 루프가 실행될 수 있으므로 충분히 가능하다고 생각함.
독특한 아이디어를 찾기 보다는 실수를 하지 않아야 하는 문제.
체크 리스트 활용이 필요했음.
"""


def solution(m, n, board):
    for i in range(m):
        board[i] = list(board[i])
    while True:
        ok = False
        check = [[False] * n for _ in range(m)]
        for y in range(m - 1):
            for x in range(n - 1):
                test = set([board[y][x], board[y + 1][x], board[y][x + 1], board[y + 1][x + 1]])
                if len(test) == 1 and board[y][x] != "0":
                    ok = True
                    check[y][x], check[y + 1][x], check[y][x + 1], check[y + 1][x + 1] = True, True, True, True
        for y in range(m):
            for x in range(n):
                if check[y][x]:
                    board[y][x] = "0"
        while True:
            changed = False
            for x in range(n):
                for y in range(m - 1, 0, -1):
                    if board[y][x] == "0" and board[y - 1][x] != "0":
                        changed = True
                        board[y][x], board[y - 1][x] = board[y - 1][x], board[y][x]
            if not changed:
                break
        if not ok:
            break
    answer = 0
    for y in range(m):
        for x in range(n):
            if board[y][x] == "0":
                answer += 1

    return answer