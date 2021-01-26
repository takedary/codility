def bm_leader(A):
  """Boyer–Moore majority vote algorithm."""
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

  cand_count = sum(a == candidate for a in A)
  if cand_count <= len(A) // 2:
    raise ValueError
  return candidate, cand_count


def solution(A):
  N = len(A)
  try:
    leader, count = bm_leader(A)
  except ValueError:
    return 0

  n_els = 0
  count_left = 0
  for i, a in enumerate(A, start=1):
    if a == leader:
      count_left += 1
    if 2 * count_left > i and 2 * (count-count_left) > N - i:
      n_els += 1
  return n_els


if __name__ == '__main__':
  cases = [
      ([4, 3, 4, 4, 4, 2],),
      ([0],),
      ([0, 1],),
      ([1, 2, 3, 4, 5],),
  ]
  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
