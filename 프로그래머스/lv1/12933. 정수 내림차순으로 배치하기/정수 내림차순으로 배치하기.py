def solution(n):
    ls = list(str(int(n)))
    ls.sort(reverse = True)
    answer = int("".join(ls))
    return answer