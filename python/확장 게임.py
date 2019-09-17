from collections import deque
from copy import deepcopy

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
n, m, p = map(int, input().split())
s = list(map(int, input().split()))
d = []
pos = [[] for i in range(p)]  # 인덱스 i는 격자판에서 숫자 i+1의 위치들
for i in range(n):
    temp = list(input())
    for j in range(m):
        if temp[j] != "." and temp[j] != "#":
            val = int(temp[j])
            pos[val - 1].append([i, j])
    d.append(temp)
while True:
    changed = False
    for i in range(p):
        q1 = deque(pos[i])
        q2 = deque()
        nextPos = []
        for j in range(s[i]):
            if not q1:
                break
            while q1:
                y, x = q1.popleft()
                for direction in range(4):
                    ny = y + dy[direction]
                    nx = x + dx[direction]
                    if 0 <= ny < n and 0 <= nx < m and d[ny][nx] == ".":
                        changed = True
                        d[ny][nx] = str(i + 1)
                        if j == s[i] - 1:
                            nextPos.append([ny, nx])
                        q2.append([ny, nx])
            q1 = deepcopy(q2)
            q2.clear()
        pos[i] = deepcopy(nextPos)
    if not changed:
        break
cnt = [0] * p
for i in range(n):
    for j in range(m):
        if d[i][j] != "." and d[i][j] != "#":
            cnt[int(d[i][j]) - 1] += 1
print(" ".join(map(str, cnt)))

'''
BFS중에서도 고난이도 문제
어떻게 하면 큐에 들어갈 요소들을 줄일 수 있는지 생각해보기
문제 조건 정확히 읽기. 특히 변수의 범위.
'''