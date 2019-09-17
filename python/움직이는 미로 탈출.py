from collections import deque

d = []
dy, dx = [-1, -1, -1, 0, 1, 1, 1, 0, 0], [-1, 0, 1, 1, 1, 0, -1, -1, 0]
for _ in range(8):
    d.append(list(input()))

q1, q2 = deque(), deque()
q1.append((7, 0))
while True:
    check = [[False] * 8 for _ in range(8)]
    if q1:
        while q1:
            y, x = q1.popleft()
            for k in range(9):
                ny, nx = y + dy[k], x + dx[k]
                if 0 <= ny < 8 and 0 <= nx < 8 and not check[ny][nx] and d[ny][nx] == ".":
                    if ny == 0 and nx == 7:
                        print(1)
                        exit()
                    check[ny][nx] = True
                    q2.append((ny, nx))
        d = [list("." * 8)] + d[:7]
        for y, x in q2:
            if d[y][x] == ".":
                q1.append((y, x))
        q2.clear()
    else:
        break
print(0)
