import sys

sys.setrecursionlimit(1501 * 1501)
a, b, c = map(int, input().split(' '))
check = [[False for i in range(1501)] for j in range(1501)]
s = a + b + c


def dfs(x, y):
    if not check[x][y]:
        check[x][y] = True
    else:
        return
    l = [x, y, s - x - y]
    for i in range(3):
        for j in range(3):
            if l[i] < l[j]:
                nl = [x, y, s - x - y]
                nl[j] -= l[i]
                nl[i] += l[i]
                dfs(nl[0], nl[1])


if s % 3 != 0:
    print(0)
else:
    dfs(a, b)
    if check[s // 3][s // 3]:
        print(1)
    else:
        print(0)

'''
경로? 를 체크하는 문제에서 리스트를 사용하는 버릇을 들여야 할 것 같다.
BFS문제로 분류되어 있는데 DFS아닌가?
아직은 문제를 많이 풀어봐야 할듯하다.
'''