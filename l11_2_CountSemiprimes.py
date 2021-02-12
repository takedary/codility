from collections import defaultdict
from itertools import accumulate
import math


def print_table(l, start=0):
  n = len(l)
  w = max(len(str(n)), len(str(max(l))))
  print(' '.join(['{:{}d}'.format(i, w) for i in range(start, start + n)]))
  print(' '.join(['{:{}d}'.format(i, w) for i in l]))


def arrayf(n):
  f = [0] * (n + 1)
  for i in range(2, int(math.sqrt(n)) + 1):
    if f[i] == 0:
      for j in range(i * i, n + 1, i):
        if f[j] == 0:
          f[j] = i
  return f

def solution(N, P, Q):
  # O(M)
  maxq = max(Q)

  # O(NloglogN)
  f = arrayf(maxq)
  #print_table(f)

  # O(N)
  pref = list(accumulate(f[i] > 0 and f[i//f[i]] == 0 for i in range(maxq+1)))
  #print_table(pref)

  # O(M)
  return [pref[q] - pref[p-1] for p, q in zip(P, Q)]


def primes(n):
  s = set(range(2, n + 1))
  for i in range(2, int(math.sqrt(n)) + 1):
    if i in s:
      s.difference_update(range(i * i, n + 1, i))
  return s

def slow_solution(N, P, Q):
  # O(M)
  maxq = max(Q)

  # make set of primes: O(N log(logN))
  s = primes(maxq // 2)
  #print(s)

  # list semiprimes: O((N/logN)^2) -- 素数定理
  semiprimes = [0] * (maxq + 1)
  for a in s:
    for b in s:
      try:
        semiprimes[a * b] = 1
      except IndexError:
        pass
  #print_table(semiprimes)

  # prefix sum: O(N)
  pref = list(accumulate(semiprimes))
  #print_table(pref)

  return [pref[q] - pref[p-1] for p, q in zip(P, Q)]


def create_f(n):
  f = defaultdict(int)
  for i in range(2, int(math.sqrt(n)) + 1):
    if not f[i]:
      for j in range(i * i, n + 1, i):
        f.setdefault(j, i)
  return f

def solution1(N, P, Q):
  N = max(Q)
  f = create_f(N)
  is_semiprime = (int(f[i] and not f[i // f[i]]) for i in range(N + 1))

  # accum[i]: num of semiprimes in range(i)
  accum = list(accumulate(is_semiprime, initial=0))

  return [accum[q+1] - accum[p] for p, q in zip(P, Q)]


if __name__ == '__main__':
  from random import randrange
  import timeit

  cases = [
      (None, [1, 4, 16, 30], [26, 10, 20, 42]),
  ]
  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
    print(f'{solution1(*c) = }')


  print('\nspeed test')

  def setup(N):
    cases = []
    for _ in range(10):
      M = 100
      P = [randrange(1, N+1) for _ in range(M)] + [N]
      Q = [randrange(p, N+1) for p in P]
      cases.append((None, P, Q))
    return cases

  def test_solution(solution, cases):
    for c in cases:
      solution(*c)

  def run_test(test_str, start, stop):
    print(test_str)
    globals_ = globals()
    for N in [10**i for i in range(start, stop)]:
      globals_['N'] = N
      times = timeit.repeat(
          test_str, 'cases = setup(N)', globals=globals_,
          repeat=5, number=1
      )
      print(f'{N = }', '{:.6f}'.format(sum(times)/50), sep='\t')

  run_test('test_solution(solution, cases)', 2, 6)
  run_test('test_solution(slow_solution, cases)', 2, 5)
  run_test('test_solution(solution1, cases)', 2, 6)
