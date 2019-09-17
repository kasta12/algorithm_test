n = int(input())
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
check = set()


def dfs(m, y, x, l, str):
    if l == 6:
        newStr = int(str + m[y][x])
        check.add(newStr);
    else:
        for i in range(4):
            if not (y + dy[i] < 0 or y + dy[i] >= 4 or x + dx[i] < 0 or x + dx[i] >= 4):
                dfs(m, y + dy[i], x + dx[i], l + 1, str + m[y][x])


for i in range(n):
    m = [input().split(' ') for j in range(4)]
    for y in range(4):
        for x in range(4):
            dfs(m, y, x, 0, '')
    print('#{} {}'.format(i + 1, len(check)))
    check.clear()

'''
전형적인 DFS 문제였다. 각 위치에서 출발해서 인접한 칸으로 이동하면서 7자리 수를 만들고 그 수의 종류가 몇개인지 구하는 문제.
너무 오랜만에 알고리즘 문제를 풀어서 적응하는데 꽤 오래 걸렸고 파이썬 문법을 떠올리는데도 오랜 시간이 걸렸다.
도달했던 경로(숫자)를 체크하는데 처음에는 리스트를 전부 조사하는 방법을 썼지만 시간초과가 발생하여 다른 8자리 리스트 선언하는 방법을 택했다.
하지만 메모리 초과 오류로 인해 이마저 사용할 수 없었고 결국 중복을 허용하지 않는 set을 사용하여 중복 제거 문제를 해결했다.
하지만 set은 mutable한 원소들만 가질 수 있으므로 경로에 두가지 변수가 사용되는 경우(y좌표와 x좌표를 담은 리스트)는 set으로 체크가 불가능해 보인다. 
이 경우 2차원 리스트를 미리 정의한 후 사용하는 수 밖에 없어보인다.
'''