def solution(N, stages):
    reach, notClear, error = [0 for _ in range(N)], [0 for _ in range(N)], []
    for step in stages:
        for i in range(step):
            if i != N:
                reach[i] += 1
        if step != N + 1:
            notClear[step - 1] += 1
    for i in range(N):
        try:
            error.append([notClear[i] / reach[i], i + 1])
        except:
            error.append([0, i + 1])
    error.sort(key=lambda x: (-x[0]))
    return [x[1] for x in error]