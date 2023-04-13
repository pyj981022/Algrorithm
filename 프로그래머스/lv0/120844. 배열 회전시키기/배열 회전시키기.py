# deque 
from collections import deque

def solution(numbers, direction):
    answer = []
    num_deque = deque(numbers)
    if direction == "right":
        #rotate() 함수의 인자로 전달한 값만큼 회전
        num_deque.rotate(1)
    else:
        # 음수를 전달하면 거꾸로 회전
        num_deque.rotate(-1)
    return list(num_deque)