import sys


def solution(A):
  ss = -sys.maxsize  # ss[q]: max sum of (P, Q) such that Q = q
  max_ss = -sys.maxsize
  for a in A:
    ss = max(ss + a, a)
    max_ss = max(ss, max_ss)
  return max_ss


if __name__ == '__main__':
  from random import randrange

  cases = [
      ([1, 3, -5, 3],),
      ([1],),
      ([-2, -3, -3],),
  ]
  for _ in range(6):
    N = randrange(1, 5)
    c = ([randrange(-10, 10) for _ in range(N)],)
    cases.append(c)

  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
