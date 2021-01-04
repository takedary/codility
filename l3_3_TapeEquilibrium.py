import sys


def solution(A):
  s = sum(A)
  cumsum = 0
  min_diff = sys.maxsize
  for a in A[:-1]:
    cumsum += a
    diff = abs(s - 2 * cumsum)
    if diff <= 1:
      return diff
    min_diff = min(min_diff, diff)

  return min_diff


if __name__ == '__main__':
  from random import randrange

  cases = [
      ([-1, 100],),
      ([3, 1, 2, 4, 3],),
  ]
  for _ in range(6):
    cases.append(([randrange(-3, 3) for _ in range(randrange(1, 5))],))

  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
