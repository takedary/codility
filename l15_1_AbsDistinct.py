def solution(A):
  return len(set(abs(a) for a in A))


def gen_unique(A, reverse=False):
  if reverse:
    A = zip(reversed(range(len(A))), reversed(A))
  else:
    A = enumerate(A)

  prev = -2147483649
  for i, a in A:
    if a != prev:
      yield i, a
      prev = a

def solution_without_set(A):
  N = len(A)
  if N == 1:
    return 1

  left, right = gen_unique(A), gen_unique(A, reverse=True)

  count = 0
  (il, al), (ir, ar) = next(left), next(right)
  while il < ir and al * ar < 0:
    count += 1
    if abs(al) == ar:
      (il, al), (ir, ar) = next(left), next(right)
    elif abs(al) > ar:
      il, al = next(left)
    else:
      ir, ar = next(right)

  count += len(list(gen_unique(A[il:ir+1])))
  return count

if __name__ == '__main__':
  from random import choices, randrange

  cases = [
      ([-5, -3, -1, 0, 3, 6],),
      ([-5, -1, -1, 0, 0, 6],),
      ([-5, -3, -3, 3, 3, 6],),
      ([-1],),
      ([0],),
      ([1],),
      ([-1, 1],),
      ([-2, -1],),
      ([1, 2],),
      ([-1, 0],),
      ([0, 1],),
      ([0, 0],),
      ([-1, 1, 1, 3],),
  ]
  for _ in range(6):
    M = randrange(10)
    N = randrange(1, 11)
    A = sorted(choices(range(-M, M + 1), k=N))
    cases.append((A,))
  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
    print(f'{solution_without_set(*c) = }')
