def solution(array):
    array.sort()
    median_array = len(array)//2
    return array[median_array]