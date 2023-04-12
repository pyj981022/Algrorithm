def solution(numbers):
    # 리스트 오름차순 정렬
    numbers.sort(reverse=True)
    
    # 가장 큰 값인 0번째 자리와 첫 번째 자리 곱하기
    return (numbers[0]*numbers[1])