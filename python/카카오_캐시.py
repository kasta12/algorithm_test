"""
최악의 경우 시간복잡도가 300만인데 크게 오래 걸리지 않는다. 아마 연산수가 적어서 그런가보다.
아니면 300만정도의 루프도 크게 걱정하지 않아도 되는것인가?
LRU알고리즘을 이해하면 쉽게 풀 수 있는 문제였다.
"""
def solution(cacheSize, cities):
    cache = []
    t = 0
    for city in cities:
        hit = False
        mint = 5 * len(cities)
        idx = -1
        for i, c in enumerate(cache):
            if c[1] < mint:  # 캐시가 miss인 경우 LRU알고리즘에 의해 교체될 idx 체크
                mint, idx = c[1], i
            if c[0] == city.upper():  # 캐시 hit인 경우
                t += 1
                hit, c[1] = True, t
                break
        if not hit:
            t += 5
            if len(cache) < cacheSize:
                cache.append([city.upper(), t])
            else:
                if idx != -1:  # 캐시가 비어있는 경우 idx가 갱신되지 않음
                    cache[idx] = [city.upper(), t]
    return t