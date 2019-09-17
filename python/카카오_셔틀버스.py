"""
O(N)
시간복잡도가 중요한 문제는 아님.
어떻게 제일 늦은 시간을 찾을것인가가 중요. 앞에서부터 조사해야 할지 뒤에서 부터 조사해야 할지 판단하는 것도 중요.
"""


def solution(n, t, m, timetable):
    tt = []
    for time in timetable:
        a, b = map(int, time.split(':'))
        tt.append(a * 60 + b)
    tt.sort(reverse=True)  # 시간의 역순으로 정렬
    for i in range(n - 1):
        e = 540 + i * t  # 각 셔틀버스 시간마다 탑승할 크루들을 선별
        for _ in range(m):
            if tt[-1] <= e:  # 현재 줄서있는 크루인 경우 탑승
                tt.pop()
            else:  # 아니라면 break
                break
    time = 540 + (n - 1) * t  # 제일 마지막 시간
    l = [i for i in tt if i <= time]  # 제일 마지막 시간에 줄서있는 크루들
    if len(l) >= m:  # 크루들의 수가 탑승제한인원보다 많거나 같은 경우
        l.sort()
        time = l[m - 1] - 1
        # 콘은 제일마지막에 탑승할 크루보다 1분만 빨리 도착하면 무조건 버스를 탈 수 있고 그 시간이 제일 늦게 버스를 타는 경우이다.
        # 콘이 어떤 버스를 타는지는 중요하지 않다.
        # 크루들의 수가 탑승제한인원보다 적으면 제일 늦은 시간인 버스 도착시간에 도착하여 버스에 탑승하면 된다.
    a, b = time // 60, time % 60
    if a < 10:
        a = "0" + str(a)
    else:
        a = str(a)
    if b < 10:
        b = "0" + str(b)
    else:
        b = str(b)

    return a + ":" + b