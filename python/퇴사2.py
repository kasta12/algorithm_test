n = int(input())
cost, money = [], []
for i in range(n):
    a, b = map(int, input().split(" "))
    cost.append(a)
    money.append(b)
acc = [0] * n
cur = 0
for i in range(n):
    if (i + cost[i] - 1) < n:
        acc[i + cost[i] - 1] = max(acc[i + cost[i] - 1], cur + money[i])
    cur = max(cur, acc[i])
print(cur)
"""
이 문제의 경우 N의 제한이 150만이었기 때문에 무조건 시간복잡도 N 이하의 알고리즘으로 풀어야 한다고 생각했다.
그래서 반복문 1회로 풀 수 있는 방법을 생각해냈다.
현재 가질 수 있는 가장 큰 값을 기억하고 미래의 값들을 예측하는 방법을 이용했다.
"""