import sys

sys.setrecursionlimit(1000000)
check = [[[[[False] * 4 for l in range(4)] for k in range(51)] for j in range(51)] for i in range(51)]
inputStr = input()
a, b, c = 0, 0, 0
for ch in inputStr:
    if ch == "A":
        a += 1
    elif ch == "B":
        b += 1
    else:
        c += 1


def dfs(p1, p2, string):
    global a, b, c
    if check[a][b][c][p1][p2]:
        return
    if len(string) == len(inputStr):
        print(string)
        exit()
    if a > 0:
        a -= 1
        dfs(p2, 1, string + "A")
        check[a][b][c][p2][1] = True
        a += 1
    if b > 0 and (len(string) == 0 or string[-1] != "B"):
        b -= 1
        dfs(p2, 2, string + "B")
        check[a][b][c][p2][2] = True
        b += 1
    if c > 0 and (
            len(string) == 0 or (len(string) == 1 and string[-1] != "C") or (string[-1] != "C" and string[-2] != "C")):
        c -= 1
        dfs(p2, 3, string + "C")
        check[a][b][c][p2][3] = True
        c += 1


dfs(0, 0, "")
print(-1)

'''
역시나 경로표시가 중요한 문제.
그냥 DFS하면 시간초과.
경로를 어떻게 효율적으로 표현할지를 생각해보자.
이번 문제의 경우 A, B, C의 남은 수 그리고 이전과 그 이전의 알파벳이 현재 상태를 결정했다.
따라서 이를 배열로 표현해 주면 된다.
'''