def solution(before, after):
    # before와 after를 정렬했을 때 값이 같은지 확인
    if sorted(before) == sorted(after):
        return 1
    else:
        return 0
        
    
    
