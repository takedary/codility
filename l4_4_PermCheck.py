def solution(A):
  s = set(range(1, len(A)+1))
  for a in A:
    try:
      s.remove(a)
    except KeyError:
      return 0
  return int(not s)


def shorter_solution(A):
  return int(set(A) == set(range(1, len(A)+1)))


if __name__ == '__main__':
  cases = [
      ([1],),
      ([2],),
      ([1, 2],),
      ([1, 1],),
      ([3, 1],),
  ]
  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
    print(f'{shorter_solution(*c) = }')
