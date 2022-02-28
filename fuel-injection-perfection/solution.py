import collections
def solution(n):
    # Your code here
    n = int(n)
    bin = collections.deque()
    while n > 0:
        r = n % 2
        n = n // 2
        bin.append(r)
    
    steps = 0
    
    while bin:
        while bin[0] == 0:
            bin.popleft()
            steps = steps + 1
        if len(bin) == 1:
            return steps
        if len(bin) == 2:
            return steps + 2
        
        if bin[1] == 0:
            bin[0] = 0
            steps = steps + 1
        else:
            steps = steps + 1
            while bin and bin[0] == 1:
                bin.popleft()
                steps = steps + 1
            if not bin:
                return steps
            bin[0] = 1
    
    return steps
            
    