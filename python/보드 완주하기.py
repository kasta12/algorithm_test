dy = [0, -1, 1, 0]
dx = [1, 0, 0, -1]
tc = 0
while True:
    try:
        n, m = map(int, input().split(" "))
    except:
        break
    tc += 1
    d = []
    numDot = 0
    answer = 999999999999
    for i in range(n):
        temp = list(input())
        for j in temp:
            if j == ".":
                numDot += 1
        d.append(temp)
    if numDot == 0:
        print("Case {}: 0".format(tc))
        continue
    check = [[False] * m for i in range(n)]


    def go(y, x, direction, visited, numGo):
        global answer

        ny = y + dy[direction]
        nx = x + dx[direction]
        if 0 <= ny < n and 0 <= nx < m and not check[ny][nx] and d[ny][nx] == ".":
            check[ny][nx] = True
            go(ny, nx, direction, visited + 1, numGo)
            check[ny][nx] = False
        else:
            cnt = 0
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < n and 0 <= nx < m and not check[ny][nx] and d[ny][nx] == ".":
                    check[ny][nx] = True
                    go(ny, nx, i, visited + 1, numGo + 1)
                    check[ny][nx] = False
                else:
                    cnt += 1
            if cnt == 4:
                if visited == numDot:
                    if numDot == 1:
                        answer = 0
                    else:
                        answer = min(answer, numGo)


    for i in range(n):
        for j in range(m):
            if d[i][j] == ".":
                for k in range(4):
                    check[i][j] = True
                    go(i, j, k, 1, 1)
                    check[i][j] = False
    if answer == 999999999999:
        answer = -1
    print("Case {}: {}".format(tc, answer))

'''
문제에 단계에 대한 규정이 모호해서 약간 시간이 소모되었지만 그리 복잡한 문제는 아니었다.
하지만 문제를 처음에 제대로 읽는 것이 항상 중요함.
'''