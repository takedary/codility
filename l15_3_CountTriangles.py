def solution(A):
  N = len(A)
  if N < 3:
    return 0

  A = sorted(A) # A.sort() is better if it's ok to mutate A.

  count = 0
  for p, ap in enumerate(A[:-2]):
    r = p + 2
    for q, aq in enumerate(A[p+1:-1], p+1):
      ap_plus_aq = ap + aq
      while r < N and ap_plus_aq > A[r]:
        r += 1
      count += r - q - 1

  return count


def slow_solution(A):
  from itertools import combinations as comb
  return sum(x + y > z for x, y, z in comb(sorted(A), 3))


def solution1(A):
  N = len(A)
  if N < 3:
    return 0
  A = sorted(A)

  count = 0
  for p, ap in enumerate(A[:-2]):
    # caterpillar on q and r
    q = p + 1
    for r, ar in enumerate(A[p+2:], p+2):
      while ap + A[q] <= ar and q < r:
        count += r - q - 1
        q += 1
    count += (N - q - 1) * (N - q) // 2

  return count


def solution2(A):
  N = len(A)
  if N < 3:
    return 0

  A = sorted(A)

  def search(start, threshold):
    """Find min idx in [start, N) such that A[idx] >= threshold."""
    if A[-1] < threshold:
      return N
    if A[start] >= threshold:
      return start

    left, right = start, N - 1
    while left < right - 1:
      mid = (left + right) // 2
      if A[mid] >= threshold:
        right = mid
      else:
        left = mid
    return right

  count = 0
  for p, ap in enumerate(A[:-2]):
    r = p + 2
    for q, aq in enumerate(A[p+1:-1], p+1):
      r = search(r, ap + aq) # find min idx in [r, N) such that ap_plus_aq <= A[idx]
      count += r - q - 1

  return count


if __name__ == '__main__':
  from random import randrange
  import timeit

  cases = [
      ([3, 7, 12, 17, 19],),
      ([7, 8, 9, 10, 11],),
      ([10, 2, 5, 1, 8, 12],),
      ([30, 23, 15, 9, 6, 4],),
      ([1, 1, 3, 3, 3, 4],),
  ]
  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
    print(f'{solution1(*c) = }')
    print(f'{solution2(*c) = }')
    print(f'{slow_solution(*c) = }')


  print('\ncollectness test')

  for _ in range(50000):
    cases.append(([randrange(1, 5) for _ in range(randrange(10))],))
  for c in cases:
    if solution(*c) == slow_solution(*c) == solution1(*c) == solution2(*c):
      continue
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
    print(f'{solution1(*c) = }')
    print(f'{solution2(*c) = }')
    print(f'{slow_solution(*c) = }')


  print('\nspeed test')

  def setup(N):
    cases = []
    for _ in range(10):
      A = [randrange(1, 100) for _ in range(N)]
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

  run_test('test_solution(solution, cases)', 1, 4)
  run_test('test_solution(slow_solution, cases)', 1, 3)
  run_test('test_solution(solution1, cases)', 1, 4)
  run_test('test_solution(solution2, cases)', 1, 4)
