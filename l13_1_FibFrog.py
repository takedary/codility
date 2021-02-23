from functools import lru_cache
import sys

sys.setrecursionlimit(10000)


def gen_fibo(m):
  """
  return fibonacci seq while <= m, ommiting first two numbers
  """
  a, b = 1, 1
  while b <= m:
    yield b
    a, b = b, a + b

def solution(A):
  if not A:
    return 1

  N = len(A)

  fibos = list(gen_fibo(N + 1))
  fibos_set = set(fibos)
  if N + 1 in fibos_set:
    return 1

  @lru_cache(maxsize=N+1)
  def min_jumps_from(start):
    """
    Return min num of jumps to reach from position `start` to the other side
    of the river (position N), or return -1 if cannot reach.
    """
    if start == N:
      return 0
    if N - start in fibos_set:
      return 1

    min_min_jumps = N + 2
    for f in reversed(fibos): ## reversed is faster??
      if (idx := start + f) < N and A[idx]:
        if (min_jumps := min_jumps_from(idx)) == 1:
          return 2
        if min_jumps > 1:
          min_min_jumps = min(min_min_jumps, min_jumps)

    return min_min_jumps + 1 if min_min_jumps < N + 2 else -1

  return min_jumps_from(-1)


def solution1(A):
  if not A:
    return 1

  N = len(A)
  if N + 1 in set(gen_fibo(N + 1)):
    return 1

  d = {-1: 0}
  def min_jumps(i):
    def points_to_check(j):
      for n in reversed(list(gen_fibo(N + 1))):
        k = j - n
        if k < -1:
          continue
        if k == -1 or A[k]:
          if d.get(k, 0) != -1:
            yield k

    try:
      return d[i]
    except KeyError:
      pass

    jumps = []
    for p in points_to_check(i):
      j = min_jumps(p)
      if j != -1:
        jumps.append(j)
      if j == 0:
        break

    if jumps:
      d[i] = min(jumps) + 1
    else:
      d[i] = -1
    return d[i]

  return min_jumps(N)


if __name__ == '__main__':
  from random import randrange, sample

  cases = [
      # (leaves, N)
      ([], 0),
      ([], 1),
      ([], 4),
      ([], 5),
      ([4, 7, 8, 13], 15),
      ([3, 4, 6], 11),
  ]
  for _ in range(6000):
    N = randrange(64)
    A = sample(range(N), randrange(N + 1))
    cases.append((A, N))
  for _ in range(60):
    N = randrange(3)
    A = sample(range(N), randrange(N + 1))
    cases.append((A, N))

  for c in cases:
    A = [0] * c[1]
    for i in c[0]:
      A[i] = 1
    c = (A,)
    if solution(*c) == solution1(*c):
      continue
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
    print(f'{solution1(*c) = }')
