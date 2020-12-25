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
  print_table(f)

  # O(N)
  pref = list(accumulate(f[i] > 0 and f[i//f[i]] == 0 for i in range(maxq+1)))
  print_table(pref)

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
  print(s)

  # list semiprimes: O((N/logN)^2) -- 素数定理
  semiprimes = [0] * (maxq + 1)
  for a in s:
    for b in s:
      try:
        semiprimes[a * b] = 1
      except IndexError:
        pass
  print_table(semiprimes)

  # prefix sum: O(N)
  pref = list(accumulate(semiprimes))
  print_table(pref)

  return [pref[q] - pref[p-1] for p, q in zip(P, Q)]


if __name__ == '__main__':
  print(slow_solution(None, [1, 4, 16, 30], [26, 10, 20, 42]))
  print(solution(None, [1, 4, 16, 30], [26, 10, 20, 42]))