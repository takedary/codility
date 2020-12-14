def check_next(peaks, next_peaks, n_flags_taken):
  #print('n_flags_taken: {}'.format(n_flags_taken))
  n_flags_set = 0
  current_position = peaks[0]
  while n_flags_set < n_flags_taken and current_position <= peaks[-1]:
    current_position = next_peaks[current_position]
    n_flags_set += 1
    current_position += n_flags_taken
  return n_flags_set == n_flags_taken

def check_naive(peaks, next_peaks, n_flags_taken):
  #print('n_flags_taken: {}'.format(n_flags_taken))
  n_flags_set = 1
  start = peaks[0]
  for p in peaks[1:]:
    #print(n_flags_set)
    if p - start >= n_flags_taken:
      n_flags_set += 1
      start = p
      if n_flags_set == n_flags_taken:
        return True
  return False

def search_binary(peaks, next_peaks, max_flags, check):
  left, right = 2, max_flags + 1
  while right - left > 1:
    mid = (left + right) // 2
    if check(peaks, next_peaks, mid):
      left = mid
    else:
      right = mid
  return left

def search_linear(peaks, next_peaks, max_flags, check):
  for n_flags_taken in range(max_flags, 2, -1):
    if check(peaks, next_peaks, n_flags_taken):
      return n_flags_taken
  return 2

def peaks2flags(peaks, N, search, check):
  #print('N: {}'.format(N))
  if N < 3:
    return 0
  #print('peaks: {}'.format(peaks))
  n_peaks = len(peaks)
  if n_peaks <= 2:
    return n_peaks

  # find maximum number of flags to check
  max_peak_distance = peaks[-1] - peaks[0]
  max_flags = n_peaks
  #print('max_flags: {}'.format(max_flags))
  while max_flags * (max_flags-1) > max_peak_distance:
    max_flags -= 1
  #print('max_flags: {}'.format(max_flags))
  if max_flags == 2:
    return 2

  # make next_peaks
  next_peaks = None
  if check == 'next':
    next_peaks = [-1] * N
    p = 0
    for i in range(N):
      if p == n_peaks:
        continue
      next_peaks[i] = peaks[p]
      if i == peaks[p]:
        p += 1
  #print('next_peaks:', next_peaks)

  # check
  search_funcs = dict(binary=search_binary, linear=search_linear)
  check_funcs = dict(next=check_next, naive=check_naive)
  #print('{} search, {} check'.format(search, check))
  res = search_funcs[search](peaks, next_peaks, max_flags, check_funcs[check])
  return res

def solution(A):
  N = len(A)
  if N < 3:
    return 0

  # find peaks
  peaks = [i for i in range(1, N-1) if A[i] > max(A[i-1], A[i+1])]
  n_peaks = len(peaks)
  #print('peaks:', peaks)
  if n_peaks <= 2:
    return n_peaks

  return peaks2flags(peaks, N, 'binary', 'next')
