def solution(n, t):
    # i가 시간별로 증가할 때
    for i in range(t):
        n = n * 2
    return n