from functools import reduce

x, y, w, s = map(int, input().split())

def solution(x,y,w,s):
  def cartesian():
    return (x+y)*w
  
  def consider_diagonal():
    def diagonal_only():
      return max(x, y) * s  

    def diagonal_mixed():
      return (max(x, y) - 1) * s + w

    if((x+y) % 2 == 0):
      return diagonal_only()
    else:
      return diagonal_mixed()
  
  def mixed_move():
    return (min(x, y) * s) + ((max(x, y) - min(x, y)) * w)
  
  return reduce(
    lambda x,y: min(x,y),
    [cartesian(), consider_diagonal(), mixed_move()]
  )

print(solution(x,y,w,s))