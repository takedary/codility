def solution(M, A):
  N = len(A)

  l = 0
  count = 0
  idx = {} # key is element of A and value is index where key appeared. A[i] = a <==> idx[a] = i.
  for r, ar in enumerate(A): # ar is A[r]
    if (last_ar := idx.setdefault(ar, r)) != r:
      # Duplication found. A[l:r] is distinct and A[r] exists in A[l:r]. A[last_ar] == A[r].

      # add (r-l + r-l-1 + r-l-2 + ... + r-last_ar) to count
      count += (r - l + r - last_ar) * (last_ar - l + 1) // 2

      # update idx
      for a in A[l:last_ar]:
        del idx[a]
      idx[ar] = r

      # move l to last_ar + 1
      l = last_ar + 1

  # A[l:N] is distinct.
  count += (N - l) * (N - l + 1) // 2

  return min(count, 1000000000)


def slow_solution(M, A):
  N = len(A)

  count = 0
  for l in range(N):
    pool = set()
    for r in range(l, N):
      if A[r] in pool:
        break
      pool.add(A[r])
      count += 1
  return count


if __name__ == '__main__':
  from random import choices, randrange

  cases = [
      (None, [4, 2, 9, 8, 0, 7, 3, 8, 7, 4]),
      (None, [3, 4, 5, 5, 2]),
      (None, [3, 4, 7, 6, 9, 1, 6, 0, 4, 9],),
      (None, [0, 0, 0]),
      (None, [0, 0, 0, 0, 0, 0, 0]),
  ]
  for _ in range(6):
    M = randrange(10)
    N = randrange(1, 11)
    A = choices(range(M + 1), k=N)
    cases.append((M, A))
  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
    print(f'{slow_solution(*c) = }')

  print('\ncorrectness test')
  cases = []
  for _ in range(600):
    M = randrange(10)
    N = randrange(1, 11)
    A = choices(range(M + 1), k=N)
    cases.append((M, A))
  for _ in range(600):
    M = randrange(1000)
    N = randrange(1, 1001)
    A = choices(range(M + 1), k=N)
    cases.append((M, A))
  for c in cases:
    if solution(*c) == slow_solution(*c):
      continue
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
    print(f'{slow_solution(*c) = }')
