def solution(sides):
    sides.sort()
    # 가장 큰 값 < 나머지 두 변의 합 → 삼각형 o
    if sides[2] < sides[0] + sides[1]:
        return 1
    else:
        return 2
    
    
    