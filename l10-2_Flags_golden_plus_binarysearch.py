from itertools import accumulate
import random


def check(peaks, next_peaks, n_flags_taken):
  print('n_flags_taken:', n_flags_taken)
  n_flags_set = 0
  current_position = peaks[0]
  while True:
    print('    current_position:', current_position)
    n_flags_set += 1
    print('    n_flags_set:', n_flags_set)
    if n_flags_set == n_flags_taken:
      return True
    if current_position + n_flags_taken <= peaks[-1]:
      current_position = next_peaks[current_position + n_flags_taken]
    else:
      return False

def solution(A):
  N = len(A)
  if N < 3:
    return 0

  # find peaks
  peaks = [i for i in range(1, N-1) if A[i] > max(A[i-1], A[i+1])]
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

  # make next_peaks
  next_peaks = []
  p = 0
  for i in range(N):
    if p == n_peaks:
      next_peaks.append(-1)
      continue
    next_peaks.append(peaks[p])
    if i == peaks[p]:
      p += 1
  print('next_peaks:', next_peaks)

  # check
  left, right = 2, max_flags + 1
  while right - left > 1:
    mid = (left + right) // 2
    if check(peaks, next_peaks, mid):
      left = mid
    else:
      right = mid
  return left


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
                  for _ in range(random.randrange(20, 1030))])
  for c in cases:
    print('\n', c)
    print(solution(c))
