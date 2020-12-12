from itertools import accumulate
import random


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
  left, right = 2, max_flags+1 # FIXME: ad hoc
  while right - left > 1:
    mid = (left + right) // 2
    if check(peaks, mid) == mid:
      left = mid
    else:
      right = mid
  return left


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


if __name__ == '__main__':
  cases = [
      [1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2],
      [1, 1, 1, 1],
      [0, 1, 0],
      [0, 1, 0, 1, 0],
      [0, 1, 0, 1, 0, 1, 0],
      [4, 3, 5, 4, 3, 5, 2, 5, 4, 2, 5, 1]
  ]
  for _ in range(5):
    cases.append([random.randrange(10)
                  for _ in range(random.randrange(20, 30))])
  for c in cases:
    print('\n', c)
    print(solution(c))
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
