from collections import deque
from copy import deepcopy

knight = [[1, 2], [2, 1], [-1, 2], [2, -1], [1, -2], [-2, 1], [-1, -2], [-2, -1]]
rook = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
bishop = [[1, 0], [-1, 0], [0, 1], [0, -1]]
n = int(input())
pos = [0] * (n * n + 1)  # i의 위치는 i-1번째 요소
d = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j, p in enumerate(temp):
        pos[p] = [i, j]
    d.append(temp)

cnt = 0
nextQ = deque()
nextQ.append((pos[1][0], pos[1][1], 0))
nextQ.append((pos[1][0], pos[1][1], 1))
nextQ.append((pos[1][0], pos[1][1], 2))

cnt = 0
for i in range(1, n * n + 1):
    check = [[[-1] * 3 for _ in range(n)] for __ in range(n)]
    q = deepcopy(nextQ)
    nextQ.clear()
    for a in q:
        y, x, c = a
        check[y][x][c] = 0
    limit = -1
    while q:
        y, x, c = q.popleft()
        if y == pos[i + 1][0] and x == pos[i + 1][1]:
            if i + 1 == n * n:
                print(cnt + check[y][x][c])
                exit()
            if limit == -1:
                limit = check[y][x][c]
                cnt += limit
                nextQ.append((y, x, c))
            elif limit == check[y][x][c]:
                nextQ.append((y, x, c))

        elif limit != -1 and check[y][x][c] > limit:
            break
        else:
            for k in range(3):
                if check[y][x][k] == -1:
                    check[y][x][k] = check[y][x][c] + 1
                    q.append((y, x, k))
            if c == 0:
                for k in range(8):
                    ny, nx = y + knight[k][0], x + knight[k][1]
                    if 0 <= ny < n and 0 <= nx < n and check[ny][nx][c] == -1:
                        check[ny][nx][c] = check[y][x][c] + 1
                        q.append((ny, nx, c))
            elif c == 1:
                for k in range(4):
                    for m in range(1,n):
                        ny, nx = y + rook[k][0]*m, x + rook[k][1]*m
                        if 0 <= ny < n and 0 <= nx < n and check[ny][nx][c] == -1:
                            check[ny][nx][c] = check[y][x][c] + 1
                            q.append((ny, nx, c))
            elif c == 2:
                for k in range(4):
                    for m in range(1, n):
                        ny, nx = y + bishop[k][0]*m, x + bishop[k][1]*m
                        if 0 <= ny < n and 0 <= nx < n and check[ny][nx][c] == -1:
                            check[ny][nx][c] = check[y][x][c] + 1
                            q.append((ny, nx, c))
