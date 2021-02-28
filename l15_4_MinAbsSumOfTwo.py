from functools import reduce
from itertools import combinations_with_replacement as comb


def solution(A):
  def abs2(x):
    return 2 * abs(x)

  if 0 in A:
    return 0

  N = len(A)

  A = sorted(A)
  #print(A)
  if A[0] >= 0 or N == 1:
    return abs2(A[0])
  if A[-1] <= 0:
    return abs2(A[-1])

  min_abs = abs2(sorted(A, key=abs)[0])

  l, r = 0, N - 1
  while l < r and A[l] * A[r] < 0:
    #print('{}, {}: {}, {}'.format(l, r, A[l], A[r]))
    min_abs = min(min_abs, abs(A[l] + A[r]))
    if abs(A[l]) < abs(A[r]):
      r -= 1
    else:
      l += 1
    if min_abs == 0:
      return 0

  return min_abs


def slow_solution(A):
  return min(abs(a + b) for a, b in comb(A, 2))


def solution1(A):
  if 0 in A:
    return 0

  N = len(A)
  if N == 1:
    return 2 * abs(A[0])

  if (min_a := min(A)) > 0:
    return 2 * min_a
  if (max_a := max(A)) < 0:
    return -2 * max_a

  A = sorted(A, key=abs)
  gen_abs_sum = (abs(a + b) for a, b in zip(A[:-1], A[1:]) if a * b < 0)

  min_abs_sum = 2 * abs(A[0])
  for abs_sum in gen_abs_sum:
    if not abs_sum:
      return 0
    min_abs_sum = min(min_abs_sum, abs_sum)
  return min_abs_sum


if __name__ == '__main__':
  from random import randrange
  import timeit

  cases = [
      ([-5, 1, 1, 3, 4],),
  ]
  for _ in range(5):
    N = randrange(1, 10)
    A = [randrange(-100, 100) for _ in range(N)]
    cases.append((A,))
  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
    print(f'{solution1(*c) = }')
    print(f'{slow_solution(*c) = }')


  print('\ncollectness test')

  for _ in range(5000):
    N = randrange(1, 100)
    A = [randrange(-100, 100) for _ in range(N)]
    cases.append((A,))

  for c in cases:
    if solution(*c) == solution1(*c) == slow_solution(*c):
      continue
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
    print(f'{solution1(*c) = }')
    print(f'{slow_solution(*c) = }')


  print('\nspeed test')

  def setup(N):
    cases = []
    for _ in range(10):
      A = [randrange(-1000 * N, 1000 * N) for _ in range(N)]
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

  run_test('test_solution(solution, cases)', 3, 6)
  run_test('test_solution(solution1, cases)', 3, 6)
  run_test('test_solution(slow_solution, cases)', 2, 4)
