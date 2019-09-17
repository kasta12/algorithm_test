from collections import deque
import sys
sys.setrecursionlimit(100000)
n = int(input())
station = []
for i in range(n + 1):
    station.append([])
for i in range(n):
    a, b = map(int, input().split())
    station[a].append(b)
    station[b].append(a)

check = [False] * (n + 1)
group = []
found = False


def dfs(p, pos):
    global found, group
    if check[pos]:
        found = True
        for idx, c in enumerate(group):
            if c == pos:
                group = group[idx:]
                return
    else:
        check[pos] = True
        group.append(pos)
        for nPos in station[pos]:
            if nPos != p:
                dfs(pos, nPos)
            if found:
                return
        check[pos] = False
        group.pop()


for i in range(1, n + 1):
    dfs(0, i)
    if found:
        break
check = [False] * (n + 1)
for idx in group:
    check[idx] = True

dist = [0] * (n + 1)
for idx in group:
    if check[idx]:
        q = deque()
        q.append(idx)
        while q:
            s = q.popleft()
            for st in station[s]:
                if not check[st]:
                    check[st] = True
                    dist[st] = dist[s] + 1
                    q.append(st)
print(" ".join(map(str, dist[1:])))
