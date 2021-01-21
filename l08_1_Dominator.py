def solution(A):
  st = []
  for a in A:
    if not st or st[-1] == a:
      st.append(a)
    else:
      st.pop()

  if not st:
    return -1

  candidate = st.pop()
  count = 0
  idx = -1
  for i, a in enumerate(A):
    if a == candidate:
      count += 1
      idx = i
  if count > len(A) // 2:
    return idx
  return -1


def another_solution(A):
  if not A:
    return -1

  candidate = A[0]
  count = 1
  for a in A[1:]:
    if a == candidate:
      count += 1
    else:
      if count > 1:
        count -= 1
      else:
        candidate = a
        count = 1

  count = 0
  idx = -1
  for i, a in enumerate(A):
    if a == candidate:
      count += 1
      idx = i
  if count > len(A) // 2:
    return idx
  return -1


if __name__ == '__main__':
  cases = [
      ([],),
      ([1, 1],),
      ([1, 2],),
      ([1, 1, 2],),
      ([1, 1, 2, 2],),
      ([1, 1, 2, 2, 3, 3, 3, 3, 3],),
      ([1, 1, 1, 2, 2, 2, 3, 3, 3],),
      ([3, 4, 3, 2, 3, -1, 3, 3],),
  ]
  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
    print(f'{another_solution(*c) = }')
