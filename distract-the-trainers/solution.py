def solution(banana_list):
    store = dict()
    pairs = []
    for i in range(len(banana_list)):
        for j in range(i+1, len(banana_list)):
            if find_loop(banana_list[i], banana_list[j]):
                add_pair(i,j,store)
    while store:
        store_len = {k:len(v) for k,v in store.items()}
        for k in store_len:
            if store_len[k] == 0:
                del store_len[k]
                del store[k]
        if not store_len:
            break
        min_key = min(store_len, key=store_len.get)
        min_list = store[min_key]
        del store_len[min_key]
        for i,_ in store_len.items():
            if i not in min_list:
                del store_len[i]
        min_key_pair = min(store_len, key=store_len.get)
        remove_pair(min_key,min_key_pair,store)
        pairs.append(min_key)
        pairs.append(min_key_pair)
    
    return len(banana_list) - len(pairs)
        


    
def remove_pair(n,m,d):
    del d[n]
    del d[m]
    for k,v in d.items():
        if n in v:
            v.remove(n)
        if m in v:
            v.remove(m)
        if len(v) == 0:
            del d[k]
        
                

def add_pair(n,m,d):
    if n in d:
        d[n].append(m)
    else:
        d[n] = [m]
    if m in d:
        d[m].append(n)
    else:
        d[m] = [n]
        
    
def find_loop(n,m):
    if n==m:
        return False
    p = n+m
    if p%2 == 1:
        return True
    while p%2==0:
        p = p //2
    if p == 1:
        return False
    return True