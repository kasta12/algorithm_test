from collections import deque

n = int(input())
l = list(map(int, input().split()))
result = deque()
for k in range(n):
    for i in range(n - k):
        found = True
        for j in range(n - k):
            if i != j and (l[i] * 2 == l[j] or l[i] == l[j] * 3):
                found = False
                break
        if found:
            result.appendleft(l.pop(i))
            break
print(" ".join(map(str, result)))

'''
n^3내의 시간으로 충분히 풀 수 있어서 그렇게 함.
하지만 n 이 커지면 다른 방법을 생각해 봐야 할듯 (3으로 나누어지는 횟수로 구간 나누기)
'''