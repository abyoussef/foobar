def solution(src, dest):
    moves = [(1,2),(1,-2),(2,1),(2,-1), (-1,-2), (-1,2),(-2,-1),(-2,1)]
    cur_steps = [src]
    steps = 0
    seen = [src]
    while cur_steps:
        if dest in cur_steps:
            return steps
        new_steps = []
        for cur in cur_steps:
            cur_x = cur % 8
            cur_y = cur // 8
            for m_x,m_y in moves:
                x = cur_x + m_x
                y = cur_y + m_y
                if x not in range(8) or y not in range(8):
                    continue
                new = cur + m_x + 8 * m_y
                
                if new <= 63 and 0 <= new and new not in seen:
                    seen.append(new)
                    new_steps.append(new)
                    if new == dest:
                        return steps + 1
        cur_steps = new_steps
        steps = steps + 1
    
    return steps