def solution(hp):
    # king_ant = 5, sub_ant = 3, low_ant = 1
    king_ant = hp // 5
    sub_ant = (hp - (5*king_ant)) //3
    low_ant = (hp - (5*king_ant) - (3*sub_ant)) // 1
    
    return king_ant + sub_ant + low_ant
            