from copy import deepcopy

dc = deepcopy
n, m, r = map(int, input().split())
d = []
for i in range(n):
    d.append(list(map(int, input().split())))
nm = min(n, m)
for i in range(nm // 2):
    group = []
    group += d[i][i:m - i]
    for j in range(1, n - 2 * i - 1):
        group.append(d[i + j][m - 1 - i])
    group += reversed(d[n - 1 - i][i:m - i])
    for j in range(n - 2 * i - 2, 0, -1):
        group.append(d[i + j][i])

    l = len(group)
    idx = r % l
    for j in range(i, m - i):
        d[i][j] = group[idx % l]
        idx += 1
    for j in range(i + 1, n - i - 1):
        d[j][m - 1 - i] = group[idx % l]
        idx += 1
    for j in range(m - i - 1, i - 1, -1):
        d[n - 1 - i][j] = group[idx % l]
        idx += 1
    for j in range(n - i - 2, i, -1):
        d[j][i] = group[idx % l]
        idx += 1

for i in d:
    print(" ".join(map(str, i)))

'''
그룹 나누기가 중요했던 부분. 집중력이 필요함
문제를 다시 한번 잘 읽자...
'''
