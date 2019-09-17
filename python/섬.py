from collections import deque
from copy import deepcopy

n, m = map(int, input().split())
l = []
for i in range(n):
    l.append(list(input()))

checkMap = [[False] * m for i in range(n)]
dy = [0, 0, 1, -1]
dx = [-1, 1, 0, 0]
islands = []
# 섬 나누기
for i in range(n):
    for j in range(m):
        if l[i][j] == '#' and not checkMap[i][j]:
            island = []
            q = deque()
            q.append([i, j])
            while q:
                node = q.popleft()
                a, b = node[0], node[1]
                if l[a][b] == '#' and not checkMap[a][b]:
                    checkMap[a][b] = True
                    island.append([a, b])
                    for k in range(4):
                        ny = a + dy[k]
                        nx = b + dx[k]
                        if 0 <= ny < n and 0 <= nx < m:
                            q.append([ny, nx])
            islands.append(island)
# 둘러싸인 섬 확인
dc = deepcopy
safe = []
surrounded = []
for island in islands:
    tempMap = dc(l)
    startNode = island[0]
    q = deque()
    q.append(startNode)
    check = False
    while q:
        node = q.popleft()
        a, b = node[0], node[1]
        if a == 0 or a == n or b == 0 or b == m:
            check = True
            break
        tempMap[a][b] = "#"
        for k in range(4):
            ny = a + dy[k]
            nx = b + dx[k]
            if 0 <= ny < n and 0 <= nx < m and tempMap[ny][nx] != "#":
                q.append([ny, nx])
    if check:
        safe.append(island)
    else:
        surrounded.append(island)
# 위험한지 체크
danger = []
safe2 = []
for island in surrounded:
    check = False
    for test in safe:
        tempMap = [["."] * m for i in range(n)]
        for node in test:
            tempMap[node[0]][node[1]] = '#'
        startNode = island[0]
        q = deque()
        q.append(startNode)
        check = False
        while q:
            node = q.popleft()
            a, b = node[0], node[1]
            if a == 0 or a == n or b == 0 or b == m:
                check = True
                break
            tempMap[a][b] = "#"
            for k in range(4):
                ny = a + dy[k]
                nx = b + dx[k]
                if 0 <= ny < n and 0 <= nx < m and tempMap[ny][nx] != "#":
                    q.append([ny, nx])
        if not check:
            danger.append(island)
            break
    if check:
        safe2.append(island)

for island in safe:
    for y,x in island:
        l[y][x] = 'O'
for island in safe2:
    for y,x in island:
        l[y][x] = 'O'
for island in danger:
    for y,x in island:
        l[y][x] = 'X'
for i in range(n):
    print("".join(l[i]))

'''
역시 카카오 문제는 복잡하고 어렵다
bfs의 연속으로 예제는 맞췄는데 1퍼센트에서 시간초과가 난다.
bfs로 섬을 처음에 나누고 안전한 섬과 둘러싸인 섬을 구분한 후
둘러싸인 섬들에 대해 안전한 섬을 하나씩 골라 그 섬이 존재할 경우 둘러싸인 섬이 안전해 지는지 체크함. 
즉 육지를 만나지 않고 바로 빠져나갈 수 있는가를 체크함.
그렇게 해서 정말로 위험한 섬을 골라냄. 하지만 딱 봐도 굉장히 오래 걸릴듯함
더 나은 로직을 찾아야 할 듯 하다.
다음에 한번 다시 풀어보자
'''