from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
dy = [-2, -2, 0, 0, 2, 2]
dx = [-1, 1, -2, 2, -1, 1]
dist = [[-1] * n for i in range(n)]
dist[r1][c1] = 0
q = deque()
q.append([r1, c1])
while q:
    y, x = q.popleft()
    if y == r2 and x == c2:
        print(dist[y][x])
        exit()
    for i in range(6):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n and dist[ny][nx] == -1:
            dist[ny][nx] = dist[y][x] + 1
            q.append([ny, nx])
print(-1)

'''
그냥 BFS기본문제
'''