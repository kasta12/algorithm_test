n, m, k = map(int, input().split(" "))
d = [[5 for i in range(n)] for j in range(n)]
dplus = []
for i in range(n):
    dplus.append(list(map(int, input().split(" "))))
age = [[[] for i in range(n)] for j in range(n)]
for i in range(m):
    r, c, a = map(int, input().split(" "))
    age[r - 1][c - 1].append(a)
dy = [-1, -1, -1, 0, 1, 1, 1, 0]
dx = [-1, 0, 1, 1, 1, 0, -1, -1]
for year in range(k):
    # 봄
    for y in range(n):
        for x in range(n):
            if age[y][x]:
                idx = -1
                for i in range(len(age[y][x])):
                    if d[y][x] >= age[y][x][i]:
                        d[y][x] -= age[y][x][i]
                        age[y][x][i] += 1
                    else:
                        idx = i
                        break
                if idx != -1:
                    dead = 0
                    for i in range(idx, len(age[y][x])):
                        dead += int(age[y][x][i] / 2)
                    age[y][x] = age[y][x][:idx]
                    # 여름
                    d[y][x] += dead

    # 가을
    for y in range(n):
        for x in range(n):
            if age[y][x]:
                for i in range(len(age[y][x])):
                    if age[y][x][i] % 5 == 0:
                        for j in range(8):
                            ny = y + dy[j]
                            nx = x + dx[j]
                            if 0 <= ny < n and 0 <= nx < n:
                                age[ny][nx] = [1] + age[ny][nx]
            # 겨울
            d[y][x] += dplus[y][x]

answer = 0
for y in range(n):
    for x in range(n):
        if age[y][x]:
            answer += len(age[y][x])
print(answer)

'''
51분23초
이전에 풀어본 적이 있는 문제지만 시간초과 때문에 시간을 조금 더 썼다.
미세한 부분이라도 시간을 최대한 줄일 수 있게 알고리즘을 짜는 연습을 하자.
'''