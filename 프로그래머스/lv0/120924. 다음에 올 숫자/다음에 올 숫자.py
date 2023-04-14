def solution(common):
    a, b, c = common[:3]
    # 등차수열
    if b - a == c - b:
        answer = common[-1] +(b-a)
    # 등비수열
    elif b // a == c // b:
        answer = common[-1]*(b//a)
    return answer