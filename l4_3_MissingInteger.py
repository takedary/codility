def solution(A):
  s = set(a for a in A if a > 0)
  if not s:
    return 1

  m = max(s)
  for i in range(1, m):
    if i not in s:
      return i
  return m + 1


if __name__ == '__main__':
  from random import randrange

  cases = [
      ([1, 2, 3],),
      ([-1, -3],),
      ([1],),
      ([2],),
  ]
  for _ in range(6):
    cases.append((
        [randrange(-4, 4) for _ in range(randrange(1, 10))],
    ))

  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
