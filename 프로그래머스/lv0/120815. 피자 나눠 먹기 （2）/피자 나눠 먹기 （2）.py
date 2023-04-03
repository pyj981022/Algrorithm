# 최소 공배수
def solution(n):
    pizza = 1
    
    # pizza 한판이 6조각이니까 6을 n으로 나눴을 때 0이 아니면 +1
    while (pizza*6) % n != 0:
        pizza += 1
    return pizza
