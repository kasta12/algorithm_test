"""
최대 36만번 루프를 돌기 때문에 문제없이 실행 가능.
역시 문자열 처리를 신경써야 하는 문제
시간처리와 문자열 처리같이 귀찮은 알고리즘을 처리해야 하는 경우가 많이 나온다.
"""


def solution(m, musicinfos):
    titles = []
    for idx, info in enumerate(musicinfos):
        start, end, title, song = info.split(",")
        s1, s2 = map(int, start.split(":"))
        e1, e2 = map(int, end.split(":"))
        duration = (e1 - s1) * 60 + (e2 - s2)
        comp = []
        lyrics = []
        for c in m:
            if c == "#":
                comp[-1] += "#"
            else:
                comp.append(c)
        for c in song:
            if c == "#":
                lyrics[-1] += "#"
            else:
                lyrics.append(c)
        lyrics = lyrics * (duration // len(lyrics)) + lyrics[:duration % len(lyrics)]
        lc = len(comp)
        ll = len(lyrics)
        comp = "".join(comp)
        for i in range(ll - lc + 1):
            if comp == "".join(lyrics[i:i + lc]):
                titles.append([title, duration, idx])
                break
    if titles:
        titles.sort(key=lambda x: (-x[1], idx))
        return titles[0][0]
    else:
        return "(None)"