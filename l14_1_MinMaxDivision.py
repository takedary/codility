from itertools import combinations_with_replacement as comb


def solution(K, M, A):
  if K == 1 or len(A) == 1:
    return sum(A)

  def evaluate(x):
    """
    return True if possible to make K blocks whose sums are all no greater than x
    """
    current_sum, nblocks = 0, 0
    for a in A:
      current_sum += a
      if current_sum > x:
        nblocks += 1
        if nblocks == K:
          return False
        current_sum = a
    return True

  left, right = max(A) - 1, sum(A)
  while right - left > 1:
    mid = (left + right) // 2
    if evaluate(mid):
      right = mid
    else:
      left = mid
  return right


def slow_solution(K, M, A):
  N = len(A)
  maxes = []
  for c in comb(range(N + 1), K - 1):
    sums = []
    for b, e in zip((0,) + c, c + (N,)):
      sums.append(sum(A[b:e]))
    maxes.append(max(sums))
  return min(maxes)


if __name__ == '__main__':
  from random import randrange

  cases = [
      (3, 5, [2, 1, 5, 1, 2, 2, 2]),
      (1, None, [2]),
      (1, None, [0]),
      (2, None, [1, 2]),
      (1, 10, [5, 3]),
      (2, None, [11, 50, 23, 39, 0]),
      (14, None, [41, 36, 55, 2, 10, 5, 26, 7]),
  ]
  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
    print(f'{slow_solution(*c) = }')

  # collectness test
  for _ in range(5000):
    N = randrange(1, 8)
    cases.append((randrange(1, N+3), None, [randrange(58) for _ in range(N)]))
  for c in cases:
    if solution(*c) == slow_solution(*c):
      continue
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
    print(f'{slow_solution(*c) = }')
