def solution(H):
  num_blocks = 0
  stack = []
  for h in H:
    while stack and h < stack[-1]:
      stack.pop()
    if (not stack) or (h > stack[-1]):
      stack.append(h)
      num_blocks += 1
  return num_blocks
