def solution(dimensions, your_position, trainer_position, distance):
    res = 0
    if distance_2(your_position, trainer_position) <= distance*distance:
        res = 1
    dirs = [[1,0], [-1,0], [0,1], [0,-1]]
    while dirs:
        for dire in dirs:
            i = dire.index(0)
            j = 1 * (1-i)
            m = abs(dire[j])
            _,end = coordinate_case(dimensions, your_position,trainer_position,dire)
            if distance_2(your_position, end) > distance*distance:
                dirs.remove(dire)
                continue
            di = copy(dire)
            ranges = [range(-1, -m+j-1, -1),range(0, m+i)]
            for r in ranges:
                for k in r:
                    di[i] = k
                    _,end = coordinate_case(dimensions, your_position,trainer_position,di)
                    if distance_2(your_position, end) > distance*distance:
                        break
                    d = direction(your_position, end)
                    ps = points(your_position, end, d, dimensions)
                    reachable = True
                    for p in ps:
                        case = find_case(dimensions, p)
                        co_1, co_2 = coordinate_case(dimensions, your_position,trainer_position,case)
                        if p == co_1 or p == co_2:
                            reachable = False
                            break
                    if reachable == True:
                        res = res + 1
            dire[j] = dire[j] + dire[j] // m
                        
                
    return res
    
def coordinate_case(dims, y_p, t_p, case):
    y_p_s = copy(y_p)
    t_p_s = copy(t_p)
    for i in {0,1}:
        if case[i] % 2 == 0:
            y_p_s[i] = case[i] * dims[i] + y_p_s[i]
            t_p_s[i] = case[i] * dims[i] + t_p_s[i]
        else:
            y_p_s[i] = case[i] * dims[i] + dims[i] - y_p_s[i]
            t_p_s[i] = case[i] * dims[i] + dims[i] - t_p_s[i]
    return y_p_s, t_p_s

def distance_2(start, end):
    return (end[0] - start[0]) * (end[0] - start[0]) + (end[1] - start[1]) * (end[1] - start[1])

def direction(start, end):
    dir_x = end[0] - start[0]
    dir_y = end[1] - start[1]
    
    gcd_x_y = gcd(abs(dir_x), abs(dir_y))
    
    return [dir_x // gcd_x_y, dir_y // gcd_x_y]

def find_case(dims, p):
    p_x = p[0]
    p_y = p[1]
    return [p_x // dims[0], p_y // dims[1]]

def gcd(a,b):
    if b > a:
        a,b = b,a
    while b > 0:
        a,b = b, a%b
    return a
    
def points(start, end, direction, dimensions):
    res = []
    x = start[0] + direction[0]
    y = start[1] + direction[1]
    while x != end[0]:
        if x % dimensions[0] != 0 and y % dimensions[1] != 0:
            res.append([x,y])
        x = x + direction[0]
        y = y + direction[1]
    return res
    
def copy(l):
    res = []
    for i in l:
        res.append(i)
    return res