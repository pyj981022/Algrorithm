h, m = map(int, input().split())

# m이 45보다 작을 때
if m < 45:
    # h가 0이 아니면  h에서 1을 빼주고, m에서 60을 더해준다.
    if h != 0:
        h -= 1
        m += 60
    # h가 0일 때 h는 23으로 설정하고, m에서 60을 더해준다.
    else:
        h = 23
        m += 60

print(h, m-45)  