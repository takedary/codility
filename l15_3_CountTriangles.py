def solution(A):
  N = len(A)
  if N <= 2:
    return 0

  A.sort()

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


if __name__ == '__main__':
  from random import randrange

  cases = [
      ([3, 7, 12, 17, 19],),
      ([7, 8, 9, 10, 11],),
      ([10, 2, 5, 1, 8, 12],),
      ([30, 23, 15, 9, 6, 4],),
      ([1, 1, 3, 3, 3, 4],),
  ]
  for _ in range(50000):
    cases.append(([randrange(1, 5) for _ in range(randrange(10))],))

  for c in cases:
    if solution(*c) == slow_solution(*c):
      continue
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
    print(f'{slow_solution(*c) = }')
