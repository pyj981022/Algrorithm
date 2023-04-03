from collections import Counter

def solution(array):
    cnt = Counter(array)
    mode_array = cnt.most_common()
    mode_result = mode_array[0][1]
    li = []
    
    for num in mode_array:
        if num[1] == mode_result:
            li.append(num[0])
    if len(li) >= 2:
        return -1
    else:
        return li[0]