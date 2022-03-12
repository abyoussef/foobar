def solution(x, y):
    x,y = max(int(x),int(y)), min(int(x), int(y))
    res = 0
    while y > 0:
        res += x // y
        x,y = y, x%y
    if x == 1:
        return str(res -1)
    else:
        return "impossible"