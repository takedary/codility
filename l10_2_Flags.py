from math import sqrt


def smarter_solution(A):
  N = len(A)
  if N <= 2:
    return 0

  def check(n_flags):
    n_flags_to_put = n_flags
    i = 0
    while i in range(N) and next_peak[i] > 0:
      i = next_peak[i]
      n_flags_to_put -= 1
      if n_flags_to_put == 0:
        return True
      i += n_flags

    return False

  is_peak = [A[i-1] < A[i] and A[i] > A[i+1] for i in range(1, N-1)]
  if (n_peaks := sum(is_peak)) <= 2:
    return n_peaks  # n_peaks >= 3 hereafter.
  is_peak = [0] + is_peak + [0]

  next_peak = []
  last_peak = -1
  for i, p in reversed(list(enumerate(is_peak))):
    if p:
      last_peak = i
    next_peak.append(last_peak)
  next_peak = next_peak[::-1]
  #print(next_peak)

  leftmost_peak, rightmost_peak = next_peak[0], max(next_peak)
  peak_range = rightmost_peak - leftmost_peak

  for n_flags in range(n_peaks, 2, -1):
    if n_flags * (n_flags - 1) > peak_range:
      continue
    if check(n_flags):
      return n_flags
  return 2


def faster_solution(A):
  N = len(A)
  if N <= 2:
    return 0

  peaks = [i for i in range(1, N-1) if A[i-1] < A[i] and A[i] > A[i+1]]
  if (n_peaks := len(peaks)) <= 2:
    return n_peaks

  max_peak_distance = peaks[-1] - peaks[0]
  max_n_flags = int(sqrt(max_peak_distance + 0.25) + 0.5)

  def check(n_flags):
    n_flags_put = 1
    last_peak = peaks[0]
    for peak in peaks[1:]:
      if peak - last_peak >= n_flags:
        n_flags_put += 1
        if n_flags_put == n_flags:
          return True
        last_peak = peak
    return False

  left, right = 2, min(max_n_flags, n_peaks) + 1
  while right - left > 1:
    mid = (left + right) // 2
    if check(mid):
      left = mid
    else:
      right = mid
  return left


if __name__ == '__main__':
  from math import log10
  from random import random, randrange
  import timeit

  cases = [
      ([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2],),
      ([1, 1, 1, 1],),
      ([0, 1, 0],),
      ([0, 1, 0, 1, 0],),
      ([0, 1, 0, 1, 0, 1, 0],),
      ([4, 3, 5, 4, 3, 5, 2, 5, 4, 2, 5, 1],),
  ]
  for _ in range(5):
    c = ([randrange(10) for _ in range(randrange(20, 30))],)
    cases.append(c)

  for c in cases:
    print(f'\n{c = }')
    print(f'{smarter_solution(*c) = }')
    print(f'{faster_solution(*c) = }')


  # speed test
  def rand_unif(left, right):
    return left + (right-left) * random()

  def rand_logunif(left, right):
    e = rand_unif(log10(left), log10(right))
    return pow(10, e)

  def generate_peaks(N):
    peak_idx = int(rand_logunif(1, N-2))

    max_gap = random() * (N - peak_idx)
    while peak_idx < N - 1:
      yield peak_idx
      peak_idx += int(rand_logunif(2, 2 + max_gap))

  def setup(N):
    cases = []
    for _ in range(10):
      A = [0] * N
      for peak_idx in generate_peaks(N):
        A[peak_idx] = 1
      cases.append((A,))
    return cases

  def test_golden(cases):
    for c in cases:
      smarter_solution(*c)

  def test_mine(cases):
    for c in cases:
      faster_solution(*c)

  def run_test(name, test_str):
    print(name)
    globals_ = globals()
    for N in [10**i for i in range(2, 7)]:
      globals_['N'] = N
      times = timeit.repeat(
          test_str, 'cases = setup(N)', globals=globals_,
          repeat=5, number=1
      )
      print(f'{N = }', '{:.6f}'.format(sum(times)/50), sep='\t')

  run_test('golden', 'test_golden(cases)')
  run_test('mine', 'test_mine(cases)')
