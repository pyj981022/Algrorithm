def solution(dots):
    # x축 좌표에 대해 x로 모으기
    x = [dot[0] for dot in dots]
    # y축 좌표에 대해 y로 모으기 
    y = [dot[1] for dot in dots]
    
    # x축 가장 큰 값에서 가장 작은 값을 빼기
    w = max(x) - min(x)
    # y축 가장 큰 값에서 가장 작은 값을 빼기
    h = max(y) - min(y)
    
    result = w*h
    return result