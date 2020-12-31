from collections import Counter
from collections import defaultdict
import sys


def solution(A):
  """
  pull-based, dict, 2d dp
  dp(i, w) means num of as used to make w
  """
  def print_dp():
    print('  ', ' '.join('{:2d}'.format(w) for w in range(W//2 + 1)))
    for i, a in enumerate([0] + list(d.keys())):
      row = ('{:2d}'.format(dp[i, w]) if (i, w) in dp else '  '
             for w in range(W//2 + 1))
      print('{:2d}'.format(a), ' '.join(row))

  if not A:
    return 0

  if len(A) == 1:
    return abs(A[0])

  A = [abs(a) for a in A]
  W = sum(A)

  d = Counter(A)
  M = len(d)

  dp = {(i, 0): 0 for i in range(M + 1)}
  for i, (a, count) in enumerate(d.items(), 1):
    for w in range(1, W//2 + 1):
      if (i-1, w) in dp:
        dp[i, w] = 0
      elif w - a >= 0 and dp.get((i, w - a), count) < count:
        dp[i, w] = dp[i, w - a] + 1

  #print_dp()
  return W - 2 * max(w for i, w in dp.keys() if i == M)


def solution_push(A):
  """
  push-based, dict, 2d dp
  dp(i, w) means num of as used to make w
  """
  if not A:
    return 0

  if len(A) == 1:
    return abs(A[0])

  A = [abs(a) for a in A]
  W = sum(A)

  d = Counter(A)
  M = len(d)

  dp = {(i, 0): 0 for i in range(M + 1)}
  for i, (a, count) in enumerate(d.items(), 1):
    for w in range(W//2 + 1):
      if (i-1, w) in dp:
        dp[i, w] = 0
      if dp.get((i, w), count) < count and w + a <= W//2:
        dp[i, w+a] = dp[i, w] + 1

  return W - 2 * max(w for i, w in dp.keys() if i == M)


def solution_list(A):
  def print_dp():
    print('  ', ' '.join('{:2d}'.format(j) for j in range(W + 1)))
    for a, r in zip([0] + list(d.keys()), dp):
      print('{:2d}'.format(a),
            ' '.join(' ' + (' ' if c == sys.maxsize else str(c)) for c in r))

  if not A:
    return 0

  N = len(A)
  if N == 1:
    return abs(A[0])

  A = [abs(a) for a in A]
  W = sum(A)

  d = defaultdict(int)
  for a in A:
    d[a] += 1
  M = len(d)

  dp = [[0] + [sys.maxsize] * (W//2) for _ in range(M + 1)]
  for i, (a, count) in enumerate(d.items(), 1):
    # dp[i][w]: how many a used to make w
    for w in range(W//2 + 1):
      if dp[i-1][w] < sys.maxsize:
        dp[i][w] = 0
      if dp[i][w] < count and w + a <= W//2:
        dp[i][w+a] = min(dp[i][w+a], dp[i][w] + 1)

  #print_dp()

  for w in range(W//2, -1, -1):
    if dp[M][w] < sys.maxsize:
      return W - 2 * w


def still_slow_solution(A):
  if not A:
    return 0

  N = len(A)
  if N == 1:
    return abs(A[0])

  A = [abs(a) for a in A]
  W = sum(A)

  d = defaultdict(int)
  for a in A:
    d[a] += 1
  M = len(d)

  dp = [[True] + [False] * W for _ in range(M + 1)]
  for i, (a, count) in enumerate(d.items(), 1):
    if a == 0:
      dp[i] = dp[i-1]
      continue
    for w in range(W + 1):
      dp[i][w] = any(dp[i-1][ww]
                     for ww in range(w - count*a, w + 1, a) if ww >= 0)

  for w in range(W//2, -1, -1):
    if dp[M][w]:
      return W - 2 * w


def slow_solution(A):
  """
  O(N**2 * max(A))
  """
  if not A:
    return 0

  N = len(A)
  if N == 1:
    return abs(A[0])

  dp = [set() for _ in range(N + 1)]
  dp[0].add(0)
  for i, a in enumerate(A, 1):
    for w in dp[i-1]:
      dp[i].add(abs(w - a))
      dp[i].add(abs(w + a))
    #print(dp[i])

  return min(dp[N])


def super_slow_solution(A):
  """
  O(N * 2**N)
  """
  N = len(A)
  if N > 30:
    raise ValueError("too long list A")

  def gen_sums():
    for i in range(1<<N):
      s = 0
      for j, a in enumerate(A):
        if i & (1<<j):
          s += a
        else:
          s -= a
      yield s

  return min(abs(s) for s in gen_sums())


if __name__ == '__main__':
  from random import randrange

  cases2 = [([randrange(-10, 10) for _ in range(10)],) for _ in range(100)]

  for c in cases2:
    if solution(*c) == solution_push(*c) == solution_list(*c) == slow_solution(*c) == still_slow_solution(*c) == super_slow_solution(*c):
      continue
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
    print(f'{super_slow_solution(*c) = }')

  cases = [
      ([3, 9, 4],),
      ([-3, -9, 4],),
  ]
  for _ in range(5):
    cases.append(([randrange(-3, 3) for _ in range(3)],))
  cases.append(([randrange(-3, 3) for _ in range(10)],))

  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
    print(f'{super_slow_solution(*c) = }')
