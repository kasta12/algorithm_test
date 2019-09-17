from collections import deque

n = int(input())
d = []
posy, posx = 0, 0
for i in range(n):
    d.append(list(map(int, input().split())))
    for j in range(n):
        if d[i][j] == 9:
            d[i][j] = 0
            posy, posx = i, j
size = 2
cnt = 0
t = 0
dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]
while True:
    q = deque()
    q.append([posy, posx])
    check = [[False] * n for i in range(n)]
    check[posy][posx] = True
    dist = [[0] * n for i in range(n)]
    fish = []
    limit = -1
    while q:
        y, x = q.popleft()
        if limit != -1 and dist[y][x] > limit:
            break
        if 0 < d[y][x] < size:
            if limit == -1:
                limit = dist[y][x]
            if dist[y][x] == limit:
                fish.append([y, x])
        else:
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < n and 0 <= nx < n and not check[ny][nx]:
                    if 0 <= d[ny][nx] <= size:
                        dist[ny][nx] = dist[y][x] + 1
                        check[ny][nx] = True
                        q.append([ny, nx])
    if fish:
        fish.sort(key=lambda x: (x[0], x[1]))
        y, x = fish[0]
        d[y][x] = 0
        posy, posx = y, x
        t += dist[y][x]
        cnt += 1
        if cnt == size:
            size += 1
            cnt = 0
    else:
        break
print(t)

'''
이전에 풀어본 문제인데 판단 미스로 시간을 많이 허비함.
key를 이용한 정렬 방법 체크하고 넘어가자.
'''
