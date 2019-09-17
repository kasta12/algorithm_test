def solution(record):
    answer, name = [], {}
    for r in record:
        l = list(r.split())
        if l[0] == "Enter" or l[0] == "Change":
            name[l[1]] = l[2]
    for r in record:
        l = list(r.split())
        if l[0] == "Enter":
            answer.append(name[l[1]] + "님이 들어왔습니다.")
        elif l[0] == "Leave":
            answer.append(name[l[1]] + "님이 나갔습니다.")
    return answer