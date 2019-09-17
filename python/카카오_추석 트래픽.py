"""
O(N^2)의 풀이방식
결국 처리량이 변하는 것은 처리시작시간과 처리종료시간이므로 그 시간에서 1초동안의 작업처리량을 구하기만 하면 된다.
종료시간을 1초씩 늘려 O(NlogN)의 시간에 해결하는 방법이 있긴 하지만 실제 코딩테스트에 나온다면 떠올리기 힘든 방법이므로 패스한다.
또한 N의 최대값이 2000이므로 제한시간 내에 해결가능하다고 판단함.
"""


def solution(lines):
    s, e = [], []
    for l in lines:
        _, a, b = l.split()
        temp = list(map(float, a.split(":")))
        time = temp[0] * 3600 + temp[1] * 60 + temp[2]
        sec = float(b[:-1])
        s.append(time - sec + 0.001)
        e.append(time)
    answer = 0
    for i in range(len(lines)):
        a = s[i]
        b = (1000 * a + 999) / 1000     # 시간 경계값 주의, 또한 부동소수점 연산 오류를 피하기 위해 식 변형 필요
        val = 0
        for j in range(len(lines)):
            if a <= s[j] <= b or a <= e[j] <= b or (s[j] < a and b < e[j]):     # 1초의 구간 안에 존재하는지 조사
                val += 1
        answer = max(answer, val)
    for i in range(len(lines)):
        a = e[i]
        b = (1000 * a + 999) / 1000
        val = 0
        for j in range(len(lines)):
            if a <= s[j] <= b or a <= e[j] <= b or (s[j] < a and b < e[j]):     # 1초의 구간 안에 존재하는지 조사
                val += 1
        answer = max(answer, val)

    return answer