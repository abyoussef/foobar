def solution(m):
    n = len(m)
    terminals = []
    loops = dict()
    paths = [[0]]
    results = dict()
    for i in range(n):
        if sum(m[i]) == 0:
            if i==0:
                return [1,1]
            terminals.append(i)
            continue
    not_terminate = True
    while not_terminate:
        not_terminate = False
        new_paths = []
        for path in paths:
            s = path[-1]
            if s in terminals:
                new_paths.append(path)
                continue
            not_terminate = True
            for i in range(n):
                new_path = path[:]
                if m[s][i] != 0:
                    if i not in new_path:
                        new_path.append(i)
                        new_paths.append(new_path)
                    else:
                        a,b = m[s][i], sum(m[s])
                        pop = new_path.pop()
                        while pop != i:
                            n_pop = new_path.pop()
                            a,b = a * m[n_pop][pop], b*sum(m[n_pop])
                            pop = n_pop
                        c = gcd(a,b)
                        a,b = a//c, b//c
                        
                        a,b = b, b-a
                        c = gcd(a,b)
                        a,b = a//c, b//c
                        
                        if i in loops:
                            loops[i].append((a,b))
                        else:
                            loops[i] = [(a,b)]
        paths = new_paths
    for i in range(len(loops)):
        a,b = 1,1
        for c,d in loops[i]:
            a,b = a*c, b*d
        den = gcd(a,b)
        loops[i] = a // den, b // den
    
    for path in paths:
        dest = path.pop()
        ter = dest
        a,b = 1,1
        while path:
            pop = path.pop()
            a,b = a * m[pop][dest], b*sum(m[pop])
            if pop in loops:
                a,b = a*loops[pop][0],b*loops[pop][1]
            dest = pop
        results[ter] = a//gcd(a,b),b//gcd(a,b)
    
    tmp = []
    lcm_ = 1
    for i in results:
        lcm_ = lcm(results[i][1],lcm_)
    
    for i in results:
        a = lcm_ // results[i][1]
        results[i] = a * results[i][0]
    final = []
    for i in terminals:
        if i in results:
            final.append(results[i])
        else:
            final.append(0)
    final.append(lcm_)
    return final


def gcd(a,b):
    if b > a:
        a,b = b,a
    while b>0:
        a,b = b , a%b
    return a

def lcm(a,b):
    return a*b // gcd(a,b)