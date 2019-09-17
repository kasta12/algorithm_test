from collections import deque
from copy import deepcopy

n, k = map(int, input().split())
i = 0
checkEven = [-1] * 500001
checkOdd = [-1] * 500001
q1 = deque()
q2 = deque()
q1.append(n)
checkEven[n] = 0

while True:
    if i % 2 == 0 and checkEven[k] != -1 and not (i - checkEven[k]) % 2:
        print(i)
        exit()
    elif i % 2 == 1 and checkOdd[k] != -1 and not (i - checkOdd[k]) % 2:
        print(i)
        exit()
    i += 1
    k += i
    if k > 500000:
        break
    while q1:
        pos = q1.popleft()
        if not (i % 2):
            for j in [pos - 1, pos + 1, pos * 2]:
                if 0 <= j <= 500000 and checkEven[j] == -1:
                    checkEven[j] = i
                    q2.append(j)
        else:
            for j in [pos - 1, pos + 1, pos * 2]:
                if 0 <= j <= 500000 and checkOdd[j] == -1:
                    checkOdd[j] = i
                    q2.append(j)
    q1 = deepcopy(q2)
    q2.clear()
print(-1)

'''
라인 코딩테스트에 나왔던 문제
그 때는 못풀었지만 오랜 시간을 투자한 끝에 풀 수 있었다.
이런문제는 안나왔으면 좋겠다. 홀수 짝수로 케이스나누고 제자리 유지가 가능하다는 것을 캐치하는 것이 중요했다.
BFS는 경우의 수가 많아지면 경로체크를 하는 것을 생각하자.
'''