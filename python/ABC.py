n, k = map(int, input().split(" "))
check = [[[[False] * 436 for k in range(31)] for j in range(31)] for i in range(31)]


def dfs(i, a, b, r, string):
    if r == k:
        print(string + "A" * (n - i))
        exit()

    if i + 1 <= n:
        if not check[i + 1][a + 1][b][r]:
            dfs(i + 1, a + 1, b, r, string + "A")
            check[i + 1][a + 1][b][r] = True
        if not check[i + 1][a][b + 1][r + a] and r + a <= k:
            dfs(i + 1, a, b + 1, r + a, string + "B")
            check[i + 1][a][b + 1][r + a] = True
        if not check[i + 1][a][b][r + a + b] and r + a + b <= k:
            dfs(i + 1, a, b, r + a + b, string + "C")
            check[i + 1][a][b][r + a + b] = True


dfs(0, 0, 0, 0, "")
print(-1)

# BFS로 풀면 메모리 초과
'''
q = deque()
q.append([0, 0, 0, 0, ""])

while q:
    i, a, b, r, string = q.popleft()
    if r == k:
        print(string + "A" * (n - i))
        exit()
    check[i][a][b][r] = True
    if i + 1 <= n:
        if not check[i + 1][a + 1][b][r]:
            q.append([i + 1, a + 1, b, r, string + "A"])
        if not check[i + 1][a][b + 1][r + a] and r + a <= k:
            q.append([i + 1, a, b + 1, r + a, string + "B"])
        if not check[i + 1][a][b][r + a + b] and r + a + b <= k:
            q.append([i + 1, a, b, r + a + b, string + 'C'])
print(-1)
'''

'''
복잡하게 접근했지만 생각보다 단순한 문제였다.
처음엔 정답문자열을 찾는 알고리즘을 찾으려 했지만 힘들다는걸 깨닫고 다른 방법을 찾음.
BFS로 하면 메모리 초과 오류가 난다. 경로 검사를 위한 check리스트가 많은 메로리를 차지하기 때문에 이러한 경우 BFS는 피해야 할 듯 하다.
DFS로 접근하여 경로검사를 해주고 다음 DFS함수로 이동할 때 조건 검사들을 모두 시행해 주면 시간을 많이 단축시킬 수 있다.
'''
