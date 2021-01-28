from itertools import accumulate


def solution(A):
  """Return max of (max(A[i:]) - A[i])."""
  if not A:
    return 0
  pref_max = accumulate(reversed(A), max)
  return max(pmax - a for pmax, a in zip(pref_max, reversed(A)))


if __name__ == '__main__':
  from random import randrange

  cases = []
  for _ in range(6):
    N = randrange(5)
    c = ([randrange(10) for _ in range(N)],)
    cases.append(c)

  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
