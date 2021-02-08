from itertools import accumulate
from math import sqrt


def second_max_divisor(N):
  for i in range(2, int(sqrt(N)) + 1):
    if N % i == 0:
      return N // i
  return 1

def solution1(A):
  N = len(A)
  if N <= 2:
    return 0

  is_peak = [int(A[i-1] < A[i] and A[i] > A[i+1]) for i in range(1, N-1)]
  is_peak = [0] + is_peak + [0]
  acc_peaks = list(accumulate(is_peak, initial=0))
  n_peaks = acc_peaks[-1]
  if n_peaks <= 1:
    return n_peaks

  max_n_blocks = min(n_peaks, second_max_divisor(N))
  if max_n_blocks == 1:
    return 1

  def has_no_peak(block_idx):
    return acc_peaks[(block_idx - 1) * bsize] == acc_peaks[block_idx * bsize]

  for n_blocks in range(max_n_blocks, 1, -1):
    if N % n_blocks != 0:
      continue

    bsize = N // n_blocks
    if any(has_no_peak(i) for i in range(1, n_blocks + 1)):
      continue
    return n_blocks

  return 1


#### slower solution

def find_divisors(N):
  divisors0, divisors1 = [], []
  d = 2
  while d * d < N:
    if N % d == 0:
      divisors0.append(d)
      divisors1.append(N//d)
    d += 1
  if d * d == N:
    divisors0.append(d)
  return divisors0 + divisors1[::-1]

def find_peaks(A, N):
  cum_p = 0
  cum_ps = [cum_p]
  max_gap, cur_gap = 0, 0
  head_gap = 0
  for i in range(1, N-1):
    if cum_p > 0:
      cur_gap += 1
    if A[i] > max(A[i-1], A[i+1]):
      cum_p += 1
      max_gap = max(cur_gap, max_gap)
      cur_gap = 0
      if cum_p == 1:
        head_gap = i + 1
    cum_ps.append(cum_p)
  cum_ps.append(cum_ps[-1])
  min_block_size = max(head_gap, (max_gap+2)//2, cur_gap+2)
  return cum_ps, min_block_size

def check_block_size(A, cum_ps, N, block_size):
  cp = [cum_ps[i * block_size - 1] for i in range(1, N // block_size + 1)]
  #print('block_size = {}, cp = {}'.format(block_size, cp))
  return cp[0] > 0 and all(c0 < c1 for c0, c1 in zip(cp[:-1], cp[1:]))

def search(A, cum_ps, N, block_sizes):
  for block_size in block_sizes:
    if check_block_size(A, cum_ps, N, block_size):
      return N // block_size
  return 1

def solution2(A):
  N = len(A)
  #print('N = {}'.format(N))
  if N <= 2:
    return 0

  divisors = find_divisors(N)
  #print('divisors = {}'.format(divisors))
  
  cum_ps, min_block_size = find_peaks(A, N)
  #print(cum_ps, min_block_size)
  if cum_ps[-1] <= 1:
    return cum_ps[-1]
  elif not divisors:
    return 1

  block_sizes = [d for d in divisors if d >= min_block_size]
  #print('block_sizes = {}'.format(block_sizes))
  return search(A, cum_ps, N, block_sizes)


if __name__ == '__main__':
  import random
  import timeit

  cases = [
      ([1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2],),
      ([1, 2, 1, 1, 2, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1, 1, 1, 2],),
      ([1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 2],),
      ([1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1],),
      ([1, 1, 1, 2, 2, 2, 1, 2, 1],),
      ([1, 2, 3, 4, 5, 6],),
      ([1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 2],),
      ([1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],),
      ([0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0],),
      ([0, 1, 0, 0, 1, 0, 0, 1, 0],),
  ]
  cases.extend([
      (random.choices([0, 1], k=random.randrange(6, 400)),)
      for _ in range(5)
  ])
  for c in cases:
    print(f'\n{c = }')
    print(f'{solution1(*c) = }')
    print(f'{solution2(*c) = }')


  # correctness test
  print('\n## correctness test')
  cases = []
  for _ in range(1000):
    A = random.choices(range(10000), k=random.randrange(1, 1000))
    cases.append((A,))
  for c in cases:
    if solution1(*c) == solution2(*c):
      continue
    print(f'\n{c = }')
    print(f'{solution1(*c) = }')
    print(f'{solution2(*c) = }')


  # speedtest
  print('\n## speed test')

  def setup(N):
    cases = []
    for _ in range(10):
      weight_1 = random.random()
      weights = [1 - weight_1, weight_1]
      A = random.choices([0, 1], weights=weights, k=N)
      cases.append((A,))
    return cases

  def test_solution(solution, cases):
    for c in cases:
      solution(*c)

  def run_test(test_str):
    print(test_str)
    globals_ = globals()
    for N in [10**i for i in range(2, 6)]:
      globals_['N'] = N
      times = timeit.repeat(
          test_str, 'cases = setup(N)', globals=globals_,
          repeat=5, number=1
      )
      print(f'{N = }', '{:.6f}'.format(sum(times)/50), sep='\t')

  run_test('test_solution(solution1, cases)')
  run_test('test_solution(solution2, cases)')
