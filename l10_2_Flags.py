from itertools import accumulate


def check(peaks, n_flags_taken):
  n_flags_set = 1
  start = peaks[0]
  flags = [start]
  for p in peaks[1:]:
    if p - start >= n_flags_taken:
      n_flags_set += 1
      flags.append(p)
      start = p
      if n_flags_set == n_flags_taken:
        break
  print('n_flags_taken = {}, flags = {}, n_flags_set = {}'.format(
        n_flags_taken, flags, n_flags_set))
  return n_flags_set

def solution(A):
  N = len(A)
  if N < 3:
    return 0

  # find peaks
  peaks = [i for i in range(1, N-1) if A[i-1] < A[i] and A[i] > A[i+1]]
  print('peaks:', peaks)
  n_peaks = len(peaks)
  if n_peaks <= 2:
    return n_peaks

  # find maximum number of flags to check
  max_peak_distance = peaks[-1] - peaks[0]
  max_flags = n_peaks
  print('max_flags:', max_flags)
  while max_flags * (max_flags-1) > max_peak_distance:
    max_flags -= 1
  print('max_flags:', max_flags)
  if max_flags == 2:
    return 2

  # check
  for n_flags_taken in range(max_flags, 2, -1):
    n_flags_set = check(peaks, n_flags_taken)
    if n_flags_set == n_flags_taken:
      return n_flags_set
  return 2


'''
def f(peaks):
  nflags = 3
  max_nflags_set = 2
  while True:
    for left in range(len(peaks)):
      count = 1
      start = peaks[left]
      flags = [start]
      for p in peaks[left+1:]:
        if p - start >= nflags:
          count += 1
          flags.append(p)
          start = p
          if count == nflags:
            break
      print('nflags = {}, left = {}, flags = {}, count = {}'.format(
            nflags, left, flags, count))
      if count > max_nflags_set:
        max_nflags_set = count
    if max_nflags_set < nflags:
      break
    nflags += 1
  return max_nflags_set

def slow_solution(A):
  # find peaks
  peaks = [i for i in range(1, len(A) - 1) if A[i-1] < A[i] and A[i] > A[i+1]]
  print('peaks:', peaks)
  if len(peaks) <= 2:
    return len(peaks)

  return f(peaks)
'''


def solution1(A):
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
  print(next_peak)

  leftmost_peak, rightmost_peak = next_peak[0], max(next_peak)
  peak_range = rightmost_peak - leftmost_peak

  for n_flags in range(n_peaks, 2, -1):
    if n_flags * (n_flags - 1) > peak_range:
      continue
    if check(n_flags):
      return n_flags
  return 2


if __name__ == '__main__':
  from random import randrange

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
    print(f'{solution1(*c) = }')
  '''
  for c in cases:
    print('\n', c)
    print(slow_solution(c))
  cases = []
  for _ in range(5):
    cases.append(list(accumulate([random.randrange(2, 16) for _ in range(15)])))
  for c in cases:
    print('\n', c)
    print(f(c))
  '''
