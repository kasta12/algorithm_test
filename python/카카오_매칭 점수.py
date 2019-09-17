def solution(word, pages):
    scores = []
    for p in pages:
        idx = 0
        ps = False
        url, basicScore, outerLink,linkScore = "", 0,[],0
        while idx < len(p):
            if p[idx] == "<":
                if p[idx:idx + 33] == '<meta property="og:url" content="':
                    i = idx + 33
                    j = i 
                    while True:
                        j += 1
                        if p[j] == '"':
                            break                            
                    url = p[i:j]
                    idx = j
                elif p[idx: idx + 9] == '<a href="':
                    i = idx + 9
                    j = i
                    while True:
                        j += 1
                        if p[j] == '"':
                            break 
                    outerLink.append(p[i:j])
                    idx = j
                ps = True
                idx += 1
            elif p[idx] == ">":
                ps = False
                idx += 1
            else:
                if ps:
                    idx += 1
                else:
                    if p[idx:idx+len(word)].upper() == word.upper() and not p[idx+len(word)].isalpha() and not p[idx-1].isalpha():
                        basicScore += 1
                        idx += len(word)
                    else:
                        idx+= 1
        try:
            linkScore = basicScore / len(outerLink)
        except:
            linkScore = 0
        scores.append([url, basicScore, outerLink, linkScore])
    for i,x in enumerate(scores):
        for link in x[2]:
            for j,y in enumerate(scores):
                if link == y[0]:
                    y[1] += x[3]
    maxIdx = 0
    for i,x in enumerate(scores):
        if  x[1] > scores[maxIdx][1]:
            maxIdx = i
    return maxIdx