from collections import Counter
from math import sqrt


def solution(A):
  """O(N*logN)."""
  n = len(A)
  max_a = max(A)
  d = [n] * (max_a + 1)
  c = Counter(A)
  for a in c:
    for i in range(1, max_a//a + 1):
      d[i * a] -= c[a]
  return [d[a] for a in A]


def slow_solution(A):
  """O(N**2)."""
  ret = [0] * len(A)
  for i, a in enumerate(A):
    for aa in A:
      if a % aa != 0:
        ret[i] += 1
  return ret


def gen_divisors(n):
  """O(sqrt(n))."""
  for i in range(1, int(sqrt(n)) + 1):
    if n % i == 0:
      yield i
      if i * i != n:
        yield n // i

def solution1(A):
  """O(N*sqrt(N))."""
  N = len(A)
  counts = Counter(A)

  n_divs = {a: sum(counts[d] for d in gen_divisors(a)) for a in counts}
  return [N - n_divs[a] for a in A]


if __name__ == '__main__':
  from random import randrange
  import timeit

  cases = [
      ([3, 1, 2, 3, 6],),
  ]
  for _ in range(100):
    N = randrange(1, 500+1)
    A = [randrange(1, 2*N+1) for _ in range(N)]
    cases.append((A,))

  for c in cases:
    if len(c[0]) > 10:
      continue
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
    print(f'{slow_solution(*c) = }')
    print(f'{solution1(*c) = }')

  print('\ncollectness test')
  for c in cases:
    if solution(*c) == slow_solution(*c) == solution1(*c):
      continue
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
    print(f'{slow_solution(*c) = }')
    print(f'{solution1(*c) = }')

  print('\nspeed test')

  def setup(N):
    cases = []
    for _ in range(10):
      A = [randrange(1, 2*N+1) for _ in range(N)]
      cases.append((A,))
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
  run_test('test_solution(slow_solution, cases)', 2, 4)
  run_test('test_solution(solution1, cases)', 2, 6)
