from collections import deque

n, m = map(int, input().split())
wall = [list(map(int, input().split())) for _ in range(m)]
group = []
groupSize = [[0] * n for _ in range(m)]
groupNum = [[-1] * n for _ in range(m)]
groupN = 0
check = [[False] * n for _ in range(m)]
dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]
for i in range(m):
    for j in range(n):
        if not groupSize[i][j]:
            q = deque()
            q.append((i, j))
            g = [(i, j)]
            check[i][j] = True
            while q:
                y, x = q.popleft()
                w = wall[y][x]
                for k in range(4):
                    w, blocked = divmod(w, 2)
                    if not blocked:
                        ny, nx = y + dy[k], x + dx[k]
                        if 0 <= ny < m and 0 <= nx < n and not check[ny][nx]:
                            q.append((ny, nx))
                            g.append((ny, nx))
                            check[ny][nx] = True
            for y, x in g:
                groupSize[y][x] = len(g)
                groupNum[y][x] = groupN
            groupN += 1

print(groupN)
maxSize = 0
maxRoom = 0
for y in range(m):
    for x in range(n):
        maxSize = max(maxSize, groupSize[y][x])
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if 0 <= ny < m and 0 <= nx < n and groupNum[y][x] != groupNum[ny][nx]:
                maxRoom = max(maxRoom, groupSize[y][x] + groupSize[ny][nx])
print(maxSize)
print(maxRoom)
