def insort(a, x, key=lambda z: z[0]):
  if not a or key(x) >= key(a[-1]):
    a.append(x)
    return
  if key(x) <= key(a[0]):
    a.insert(0, x)
    return

  left, right = 0, len(a) - 1
  while right - left > 1:
    mid = (left + right) // 2
    if key(a[mid]) > key(x):
      right = mid
    else:
      left = mid
  a.insert(right, x)

def solution(R, B):
  A = sorted(
      [(x, y, 'r') for x, y in R] + [(x, y, 'b') for x, y in B],
      key=lambda z: (z[0], z[2])
  )
  print(A)

  def make_pair_if_possible(rs, coord):
    x, y = coord
    if not rs or rs[0][1] >= y:
      return

    nonlocal counter
    counter += 1
    if rs[-1][1] < y:
      _ = rs.pop()
      return
    left, right = 0, len(rs) - 1
    while right - left > 1:
      mid = (left + right) // 2
      if rs[mid][1] >= y:
        right = mid
      else:
        left = mid
    _ = rs.pop(left)

  counter = 0
  rs = []
  for x, y, c in A:
    print(x, y, c, end='')
    if c == 'r':
      insort(rs, (x, y), key=lambda z: z[1])
    else:
      make_pair_if_possible(rs, (x, y))
    print('\t', rs)

  return counter


if __name__ == '__main__':
  from random import randrange
  cases = [
      ([(1, 2), (6, 1), (6, 6), (3, 5)], [(4, 7), (3, 4), (5, 2), (2, 6)]),
      ([(1, 1)], [(2, 2)]),
      ([(2, 2)], [(1, 1)]),
      ([(2, 2)], [(2, 1)]),
      ([(2, 1)], [(2, 2)]),
      ([(1, 1), (1, 4)], [(2, 2), (2, 3)]),
  ]
  for _ in range(5):
    N = randrange(1, 5)
    cases.append((
        [(randrange(1, 10), randrange(1, 10)) for _ in range(N)],
        [(randrange(1, 10), randrange(1, 10)) for _ in range(N)]
    ))

  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
