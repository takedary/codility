def solution(A):
  N = len(A)
  if N <= 2:
    return 0

  A = sorted(A) # A.sort() is better if it's ok to mutate A.

  count = 0
  for p, a in enumerate(A[:-2]):
    r = p + 2
    for q, b in enumerate(A[p+1:-1], p+1):
      apb = a + b
      while r < N and apb > A[r]:
        r += 1
      count += r - q - 1
      #print(p, q, r, count)

  return count


def slow_solution(A):
  from itertools import combinations as comb
  return sum(x + y > z for x, y, z in comb(sorted(A), 3))


def solution1(A):
  N = len(A)
  if N < 3:
    return 0
  A = sorted(A)
  #print(A)

  count = 0
  for p, ap in enumerate(A[:N-2]):
    # caterpillar on q and r
    q = p + 1
    for r, ar in enumerate(A[p+2:], p+2):
      while ap + A[q] <= ar and q < r:
        count += r - q - 1
        q += 1
    count += (N - q - 1) * (N - q) // 2

  return count


if __name__ == '__main__':
  from random import randrange

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
    print(f'{slow_solution(*c) = }')

  for _ in range(50000):
    cases.append(([randrange(1, 5) for _ in range(randrange(10))],))
  for c in cases:
    if solution(*c) == slow_solution(*c) == solution1(*c):
      continue
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
    print(f'{solution1(*c) = }')
    print(f'{slow_solution(*c) = }')
