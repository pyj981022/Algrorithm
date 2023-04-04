def solution(price):

    # 10만원 이상, 30만원 미만
    if price >= 100000 and price < 300000:
        return int(price*0.95)
    # 30만원 이상, 50만원 미만
    elif price >= 300000 and price < 500000:
        return int(price*0.9)
    # 50만원 이상
    elif price >= 500000:
        return int(price*0.8)
    else:
        return int(price)