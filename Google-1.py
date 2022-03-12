"""

Task

0 1 1 E 1
0 S 0 0 1

0 - empty cell
1 - wall
S - start point
E - end point

Shotest path from S to E? Minimum number of steps from S to E.

moves: up, down, left, right

"""
"""
m = [
  [ 0 1 1 0 1],
  [ 0 0 0 0 1],...
]
S = (1,1)
E = (0,3)

len(m) = N 
for each i in range(N):
  len(m[i]) = K
shape(m) = N * K 
"""
"""
m_i,j  with i index row and j index column
"""

# [[S 0 E]
#  [0 1 1]]

def solution(m, s, e):
  moves = [(-1,0), (1,0), (0,1), (0,-1)]
  steps = 0
  seen = {s}
  cur_pos = {s}
  while cur_pos:
    if e in cur_pos:
      return steps
    new_pos = {}
    for cur in cur_pos:
      for i,j in moves:
        x = cur[0] + i
        y = cur[1] + j
        if x in range(len(m)):
          if y in range(len(m[x])):
            if m[x][y] == 1:
              continue
            else:
              if (x,y) not in seen:
                new_pos.add((x,y))
                seen.add((x,y))
    print(new_pos)
    cur_pos = new_pos
    steps = steps + 1
  
  return None

# m = [[0 0 0],
#      [0 1 1]]
# s = (0,0)
# e = (0,2)
# > solution(m,s,e)
# {(0,0)} // steps = 0
# {(0,1), (1,0)} // steps = 1
# {(0,2)} // steps = 2
# return 2

#complexity: O(N*K)
# O(N*K)
  
  
  





