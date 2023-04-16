def solution(absolutes, signs):
    answer = 0
    
    for i in range(len(absolutes)):
        # 양수일 때
        if signs[i]:
            answer += absolutes[i]
        # 음수일 때
        else:
            answer -= absolutes[i]
    return answer