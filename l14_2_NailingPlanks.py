def solution(A, B, C):
  M = len(C)

  def evaluate(m):
    print('eval', m)
    # return True if possible to nail all planks using C[:m]
    c = set(C[:m])
    pref, cur = [0], 0
    for i in range(max(max(A), max(B)) + 1):
      if i in c:
        cur += 1
      pref.append(cur)
    print(pref)

    for a, b in zip(A, B):
      if pref[b+1] - pref[a] == 0:
        return False
    return True

  if not evaluate(M):
    return -1

  left, right = 0, M
  while right - left > 1:
    mid = (left + right) // 2
    if evaluate(mid):
      right = mid
    else:
      left = mid
  return right


if __name__ == '__main__':
  cases = [
      ([1], [8], [3, 5, 6]),
      ([1, 6], [3, 8], [3, 5, 6]),
      ([1, 5], [3, 8], [3, 5, 6, 8]),
      ([1, 5], [2, 8], [3, 5, 6, 8]),
  ]
  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
