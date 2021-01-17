def solution(S):
  lefts = 0
  for s in S:
    if s == '(':
      lefts += 1
    else:
      if lefts == 0:
        return 0
      lefts -= 1
  return int(lefts == 0)
