def solution(arr):
    answer = []
    # arr의 길이가 2부터일 때, 가장 작은 요소 삭제
    if len(arr) > 1:
        arr.remove(min(arr))
        return arr
    else:
        return [-1]
        