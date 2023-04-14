def solution(id_pw, db):
    answer = ''
    
    # for문으로 db는 1차원 배열로 변경
    for i in db:
        # id_pw의 아이디가 db안에 있을 때
        if id_pw[0] in i:
            # 비밀번호까지 같으면 login
            if id_pw[1] == i[1]:
                return "login"
            else:
                return "wrong pw"
    return "fail"