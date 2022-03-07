import numpy as np
from fractions import Fraction as F
def solution(m):
    n = len(m)
    sums = np.sum(m,axis=1)
    ab_states = sums == 0
    tr_states = np.logical_not(ab_states)
    if ab_states[0]:
        return [1,1]
    for i in range(n):
        for j in range(n):
            if ab_states[i]:
                m[i][j] = F(0)
            else:
                m[i][j] = F(m[i][j],sums[i])
    m = np.array(m)
    Q = m[np.ix_(tr_states,tr_states)]
    tr = np.sum(tr_states)
    Fi = make_id(tr) - Q
    Fi = np.concatenate((Fi,make_id(tr)), axis=1)
    for i in range(tr):
        if Fi[i][i] != F(1,1):
            Fi[i] = Fi[i] / Fi[i][i]
        for j in range(tr):
            if j != i:
                Fi[j] = Fi[j] - Fi[j][i] * Fi[i]
    Fi = Fi[:,tr:]
    R = m[np.ix_(tr_states, ab_states)]
    finals = np.matmul(Fi,R)[0]
    nums = []
    dens = []
    
    for f in finals:
        num, den = f.numerator, f.denominator
        if num != 0:
            num, den = num / gcd(num,den), den / gcd(num,den)
        nums.append(num)
        dens.append(den)
    lcm_ = 1
    for den in dens:
        lcm_ = lcm(lcm_,den)
    results = []
    for num, den in zip(nums,dens):
        if num == 0:
            results.append(0)
        else:
            results.append(lcm_ * num // den)
    results.append(lcm_)
    results = list(map(int,results))
    return results

def gcd(a,b):
    if b > a:
        a,b = b,a
    while b>0:
        a,b = b , a%b
    return a
    
def make_id(n):
    res = []
    for i in range(n):
        tmp = []
        for j in range(n):
            if i == j:
                tmp.append(F(1))
            else:
                tmp.append(F(0))
        res.append(tmp)
    return np.array(res)

def lcm(a,b):
    return a*b // gcd(a,b)