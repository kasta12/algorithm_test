from collections import deque

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
n, m = map(int, input().split())
d = [list(input()) for _ in range(n)]
check = [[[[False] * 20 for _ in range(20)] for __ in range(20)] for ___ in range(20)]
c1, c2 = (), ()
for i in range(n):
    for j in range(m):
        if d[i][j] == "o":
            if not c1:
                c1 = (i, j)
            else:
                c2 = (i, j)

check[c1[0]][c1[1]][c2[0]][c2[1]] = True
check[c2[0]][c2[1]][c1[0]][c1[1]] = True
q = deque()
q.append((c1[0], c1[1], c2[0], c2[1], 0))
while q:
    c1y, c1x, c2y, c2x, t = q.popleft()
    if t == 10:
        print(-1)
        exit()
    for k in range(4):
        nc1y = c1y + dy[k]
        nc1x = c1x + dx[k]
        nc2y = c2y + dy[k]
        nc2x = c2x + dx[k]
        cnt = 0
        if 0 <= nc1y < n and 0 <= nc1x < m:
            if d[nc1y][nc1x] == "#":
                nc1y = c1y
                nc1x = c1x
        else:
            cnt += 1
        if 0 <= nc2y < n and 0 <= nc2x < m:
            if d[nc2y][nc2x] == "#":
                nc2y = c2y
                nc2x = c2x
        else:
            cnt += 1
        if cnt == 0:
            if c1y != nc1y or c1x != nc1x or c2y != nc2y or c2x != nc2x:
                if not check[nc1y][nc1x][nc2y][nc2x]:
                    check[nc1y][nc1x][nc2y][nc2x] = True
                    check[nc2y][nc2x][nc1y][nc1x] = True
                    q.append((nc1y, nc1x, nc2y, nc2x, t + 1))
        elif cnt == 1:
            print(t + 1)
            exit()
print(-1)
