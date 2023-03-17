def substr(s:str):
    if len(s) == 0:
        return 0
    track = ""
    count_ar = list()
    for i in range(len(s)):
        if i == len(s) - 1:
            count_ar.append(len(track) + 1) if s[i] not in track  else count_ar.append(len(track))
            # reverse
            for j in range(len(s) - 1,-1,-1):
                if j == 0:
                    count_ar.append(len(track) + 1) if s[j] not in track  else count_ar.append(len(track))
                elif s[j] in track:
                    count_ar.append(len(track))
                    track = ""
                else:
                    track += s[j]
        elif s[i] in track:
            count_ar.append(len(track))
            track = ""
        else:
            track += s[i]
    return max(count_ar)

def median(l1=[],l2=[]):
    ar = l1 + l2
    if len(ar) == 0:
        return 0
    if len(ar) % 2 == 0:
        return (ar[int(len(ar)/2)] + ar[int(len(ar)/2) - 1]) / 2
    elif len(ar) % 2 != 0:
        return ar.index(ar[int(len(ar)/2)]) + 1

print(median([1,3],[2]))



