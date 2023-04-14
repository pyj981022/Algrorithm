def solution(chicken):
    answer = 0
    
    while chicken >= 10:
        free = chicken // 10
        mod = chicken % 10
        answer += free
        chicken = free+mod
    return answer