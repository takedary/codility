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
  print('block_size = {}, cp = {}'.format(block_size, cp))
  return cp[0] > 0 and all(c0 < c1 for c0, c1 in zip(cp[:-1], cp[1:]))

def search(A, cum_ps, N, block_sizes):
  for block_size in block_sizes:
    if check_block_size(A, cum_ps, N, block_size):
      return N // block_size
  return 1

def solution(A):
  N = len(A)
  print('N = {}'.format(N))
  if N <= 2:
    return 0

  divisors = find_divisors(N)
  print('divisors = {}'.format(divisors))
  
  cum_ps, min_block_size = find_peaks(A, N)
  print(cum_ps, min_block_size)
  if cum_ps[-1] <= 1:
    return cum_ps[-1]
  elif not divisors:
    return 1

  block_sizes = [d for d in divisors if d >= min_block_size]
  print('block_sizes = {}'.format(block_sizes))
  return search(A, cum_ps, N, block_sizes)


if __name__ == '__main__':
  import random
  cases = [
      [1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2],
      [1, 2, 1, 1, 2, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1, 1, 1, 2],
      [1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 2],
      [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1],
      [1, 1, 1, 2, 2, 2, 1, 2, 1],
      [1, 2, 3, 4, 5, 6],
      [1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 2],
      [1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
      [0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0]
  ]
  cases.extend([
      random.choices([0, 1], k=random.randrange(6, 400))
      for _ in range(5)
  ])
  for c in cases:
    print()
    print(c)
    print(solution(c))
