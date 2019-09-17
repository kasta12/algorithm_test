n, m = map(int, input().split())
dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
b = []
for i in range(n):
    b.append(list(map(int, input().split())))

for y in range(n):
    for x in range(m):
        b[y][x] = [True] * b[y][x] + [False] * (101 - b[y][x])
answer = n*m*2
for y in range(n):
    for x in range(m):
        for z in range(101):
            if b[y][x][z]:
                val = 4
                for k in range(4):
                    ny, nx = y + dy[k], x + dx[k]
                    if 0 <= ny < n and 0 <= nx < m and b[ny][nx][z]:
                        val -= 1
                answer += val
print(answer)
