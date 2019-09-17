n = int(input())
s = []
for i in range(n):
    s.append(list(map(int, input().split(" "))))
t = [False] * n
minVal = 99999999999


def dfs(cur, cnt, half):
    global minVal
    if cnt == half:
        score1, score2 = 0, 0
        for i in range(n):
            if t[i]:
                for j in range(n):
                    if t[j]:
                        score1 += s[i][j]
        for i in range(n):
            if not t[i]:
                for j in range(n):
                    if not t[j]:
                        score2 += s[i][j]
        val = score1 - score2 if score1 > score2 else score2 - score1
        minVal = min(minVal, val)
    else:
        if n - cur + cnt < half:  # 남은 선수들을 다 팀으로 포함시켜도 half명이 되지 않으면 종료
            return
        # cur 선택
        t[cur] = True
        dfs(cur + 1, cnt + 1, half)
        t[cur] = False
        # cur 선택 X
        dfs(cur + 1, cnt, half)


for i in range(1, int(n / 2) + 1):
    dfs(0, 0, i)
print(minVal)

'''
두 팀중 한 팀이 1 ... n/2 명이 되는 경우에 대해 DFS를 실행하여 팀 구성
n이 짝수인 경우 중복되는 경우가 생기지만 제일 마지막 경우에만 생기는 경우이기 때문에 따로 최적화 작업을 하지 않음
그럼 만약 해야 한다면 어떻게? 그런데 더 복잡해지기만 할 듯하다.
'''
