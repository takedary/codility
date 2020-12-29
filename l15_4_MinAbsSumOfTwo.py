def solution(A):
  def abs2(x):
    return 2 * abs(x)

  if 0 in A:
    return 0

  N = len(A)

  A.sort()
  print(A)
  if A[0] >= 0 or N == 1:
    return abs2(A[0])
  if A[-1] <= 0:
    return abs2(A[-1])

  min_abs = abs2(sorted(A, key=abs)[0])

  l, r = 0, N - 1
  while l < r and A[l] * A[r] < 0:
    print('{}, {}: {}, {}'.format(l, r, A[l], A[r]))
    min_abs = min(min_abs, abs(A[l] + A[r]))
    if abs(A[l]) < abs(A[r]):
      r -= 1
    else:
      l += 1
    if min_abs == 0:
      return 0

  return min_abs


def slow_solution(A):
  return min(abs(a + b) for a in A for b in A)


if __name__ == '__main__':
  from random import randrange

  cases = [
      ([-5, 1, 1, 3, 4],),
  ]
  for _ in range(5):
    cases.append(([randrange(-100, 100) for _ in range(randrange(1, 10))],))
  #for _ in range(5000):
  #  cases.append(([randrange(-100, 100) for _ in range(randrange(1, 100))],))

  for c in cases:
    #if solution(*c) == slow_solution(*c):
    #  continue
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
