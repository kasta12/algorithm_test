from collections import deque

n, m = map(int, input().split())
ladderSnake = [0] * 101
for i in range(n + m):
    a, b = map(int, input().split())
    ladderSnake[a] = b

q = deque()
q.append(1)
dist = [-1] * 101
dist[1] = 0
while q:
    pos = q.popleft()
    if pos == 100:
        print(dist[100])
        exit()
    if ladderSnake[pos]:
        dist[ladderSnake[pos]] = dist[pos]
        q.appendleft(ladderSnake[pos])
        continue
    go = []
    for i in range(1, 7):
        if pos + i > 100:
            break
        else:
            if ladderSnake[pos + i] and dist[pos + i] == -1:
                dist[pos + i] = dist[pos] + 1
                q.append(pos + i)
            else:
                go.append(i)
    while go:
        i = go.pop()
        if dist[pos + i] == -1:
            dist[pos + i] = dist[pos] + 1
            q.append(pos + i)
            break

'''
거의 두시간 걸림
뱀을 통해서 더 빨리 도달할 수 없다는 결론을 스스로 내리고 풀어서 큰 시간을 잡아먹음.
BFS의 경우 리스트에 들어가는 원소의 수를 최대한 줄여야 메모리 초과 오류를 막을 수 있다.
dist를 잘 활용해보자.
'''