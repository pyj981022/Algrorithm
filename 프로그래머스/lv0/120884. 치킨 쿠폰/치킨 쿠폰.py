def solution(chicken):
    answer = 0
    
    while chicken >= 10:
        # 서비스 치킨 마리수
        free = chicken // 10
        # 남은 쿠폰 수
        mod = chicken % 10
        answer += free
        chicken = free+mod
    return answer
