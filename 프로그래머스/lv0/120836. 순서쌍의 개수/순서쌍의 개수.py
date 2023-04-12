def solution(n):
    # 순서쌍을 담을 배열
    lst = []
    for i in range(1, n+1):
        if n % i == 0:
            lst.append([(i, n//i)])
    return len(lst)