r, c, n = map(int, input().split())
d = []
dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
check1 = [[False] * c for i in range(r)]
check2 = [[False] * c for i in range(r)]
for i in range(r):
    temp = list(input())
    for j in range(c):
        if temp[j] == "O":
            check2[i][j] = True
    d.append(temp)
timer = 1
while True:
    if timer == n:
        break

    # 설치 1
    for i in range(r):
        for j in range(c):
            if d[i][j] == ".":
                d[i][j] = "O"
                check1[i][j] = True
    timer += 1

    if timer == n:
        break

    # 폭발 1
    for i in range(r):
        for j in range(c):
            if check2[i][j]:
                check2[i][j] = False
                d[i][j] = "."
                for k in range(4):
                    ny, nx = i + dy[k], j + dx[k]
                    if 0 <= ny < r and 0 <= nx < c and not check2[ny][nx]:
                        d[ny][nx] = "."
                        check1[ny][nx] = False
    timer += 1

    if timer == n:
        break

    # 설치 2
    for i in range(r):
        for j in range(c):
            if d[i][j] == ".":
                d[i][j] = "O"
                check2[i][j] = True
    timer += 1

    if timer == n:
        break

    # 폭발 2
    for i in range(r):
        for j in range(c):
            if check1[i][j]:
                check1[i][j] = False
                d[i][j] = "."
                for k in range(4):
                    ny, nx = i + dy[k], j + dx[k]
                    if 0 <= ny < r and 0 <= nx < c and not check1[ny][nx]:
                        d[ny][nx] = "."
                        check2[ny][nx] = False
    timer += 1

for i in range(r):
    print("".join(d[i]))
