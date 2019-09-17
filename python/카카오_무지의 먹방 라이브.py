from copy import deepcopy


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    ft = deepcopy(food_times)
    ft.sort()
    prev, cur, left = 0, 0, 0
    for n in range(len(ft)):
        ok = True
        if ft[n] > prev:
            diff = ft[n] - prev
            if k >= diff * (len(food_times) - n):
                k -= diff * (len(food_times) - n)
            else:
                cur = ft[n]
                left = k % (len(food_times) - n)
                ok = False
        if not ok:
            break
        else:
            prev = ft[n]
    for idx, f in enumerate(food_times):
        if f >= cur:
            if left == 0:
                return idx + 1
            else:
                left -= 1