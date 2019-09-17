from collections import deque


def solution(board):
    n = len(board)
    dist = [[[[-1] * n for j in range(n)] for k in range(n)] for l in range(n)]
    # print(dist[n - 1][n - 1][n - 1][n - 1])
    q = deque()
    dist[0][0][0][1] = 0
    dist[0][1][0][0] = 0
    q.append((0, 0, 0, 1))
    dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
    while q:
        y1, x1, y2, x2 = q.popleft()
        if y1 == n - 1 and x1 == n - 1:
            return dist[y1][x1][y2][x2]
        if y2 == n - 1 and x2 == n - 1:
            return dist[y1][x1][y2][x2]
        for k in range(4):
            ny1, nx1, ny2, nx2 = y1 + dy[k], x1 + dx[k], y2 + dy[k], x2 + dx[k]
            if 0 <= ny1 < n and 0 <= nx1 < n and 0 <= ny2 < n and 0 <= nx2 < n and board[ny1][nx1] == 0 and board[ny2][
                nx2] == 0 and (dist[ny1][nx1][ny2][nx2] == -1):
                dist[ny1][nx1][ny2][nx2] = dist[y1][x1][y2][x2] + 1
                dist[ny2][nx2][ny1][nx1] = dist[y1][x1][y2][x2] + 1
                q.append((ny1, nx1, ny2, nx2))
        if y1 == y2:
            nx = min(x1, x2)
            if y1 + 1 < n and board[y1 + 1][nx] != 1 and dist[y1 + 1][max(x1, x2)][y2][max(x1, x2)] == -1:
                dist[y1 + 1][max(x1, x2)][y2][max(x1, x2)] = dist[y1][x1][y2][x2] + 1
                dist[y1][max(x1, x2)][y2 + 1][max(x1, x2)] = dist[y1][x1][y2][x2] + 1
                q.append((y1 + 1, max(x1, x2), y2, max(x1, x2)))
            nx = max(x1, x2)
            if y1 + 1 < n and board[y1 + 1][nx] != 1 and dist[y1 + 1][min(x1, x2)][y2][min(x1, x2)] == -1:
                dist[y1 + 1][min(x1, x2)][y2][min(x1, x2)] = dist[y1][x1][y2][x2] + 1
                dist[y1][min(x1, x2)][y2 + 1][min(x1, x2)] = dist[y1][x1][y2][x2] + 1
                q.append((y1 + 1, min(x1, x2), y2, min(x1, x2)))
            nx = min(x1, x2)
            if y1 - 1 >= 0 and board[y1 - 1][nx] != 1 and dist[y1 - 1][max(x1, x2)][y2][max(x1, x2)] == -1:
                dist[y1 - 1][max(x1, x2)][y2][max(x1, x2)] = dist[y1][x1][y2][x2] + 1
                dist[y1][max(x1, x2)][y2 - 1][max(x1, x2)] = dist[y1][x1][y2][x2] + 1
                q.append((y1 - 1, max(x1, x2), y2, max(x1, x2)))
            nx = max(x1, x2)
            if y1 - 1 >= 0 and board[y1 - 1][nx] != 1 and dist[y1 - 1][min(x1, x2)][y2][min(x1, x2)] == -1:
                dist[y1 - 1][min(x1, x2)][y2][min(x1, x2)] = dist[y1][x1][y2][x2] + 1
                dist[y1][min(x1, x2)][y2 - 1][min(x1, x2)] = dist[y1][x1][y2][x2] + 1
                q.append((y1 - 1, min(x1, x2), y2, min(x1, x2)))
            #######################################################
        if x1 == x2:
            ny = min(y1, y2)
            if x1 - 1 >= 0 and board[ny][x1 - 1] != 1 and dist[max(y1, y2)][x1 - 1][max(y1, y2)][x2] == -1:
                dist[max(y1, y2)][x1 - 1][max(y1, y2)][x2] = dist[y1][x1][y2][x2] + 1
                dist[max(y1, y2)][x1][max(y1, y2)][x2 - 1] = dist[y1][x1][y2][x2] + 1
                q.append((max(y1, y2), x1 - 1, max(y1, y2), x2))
            ny = max(y1, y2)
            if x1 - 1 >= 0 and board[ny][x1 - 1] != 1 and dist[min(y1, y2)][x1 - 1][min(y1, y2)][x2] == -1:
                dist[min(y1, y2)][x1 - 1][min(y1, y2)][x2] = dist[y1][x1][y2][x2] + 1
                dist[min(y1, y2)][x1][min(y1, y2)][x2 - 1] = dist[y1][x1][y2][x2] + 1
                q.append((min(y1, y2), x1 - 1, min(y1, y2), x2))
            ny = min(y1, y2)
            if x1 + 1 < n and board[ny][x1 + 1] != 1 and dist[max(y1, y2)][x1 + 1][max(y1, y2)][x2] == -1:
                dist[max(y1, y2)][x1 + 1][max(y1, y2)][x2] = dist[y1][x1][y2][x2] + 1
                dist[max(y1, y2)][x1][max(y1, y2)][x2 + 1] = dist[y1][x1][y2][x2] + 1
                q.append((max(y1, y2), x1 + 1, max(y1, y2), x2))
            ny = max(y1, y2)
            if x1 + 1 < n and board[ny][x1 + 1] != 1 and dist[min(y1, y2)][x1 + 1][min(y1, y2)][x2] == -1:
                dist[min(y1, y2)][x1 + 1][min(y1, y2)][x2] = dist[y1][x1][y2][x2] + 1
                dist[min(y1, y2)][x1][min(y1, y2)][x2 + 1] = dist[y1][x1][y2][x2] + 1
                q.append((min(y1, y2), x1 + 1, min(y1, y2), x2))

print(solution([[0,0],[0,0]]))
