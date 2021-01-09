from itertools import accumulate


def solution(A):
  N = len(A)
  pref = list(accumulate(A, initial=0))

  min_avg, ret = pref[2] / 2, 0
  for p in range(N-1):
    for q in (p+1, p+2):
      if q < N:
        if (avg := (pref[q+1]-pref[p]) / (q-p+1)) < min_avg:
          min_avg, ret = avg, p

  return ret


def solution2(A):
  min_avg, ret = sum(A[:2]) / 2, 0
  for p, ap in enumerate(A[:-1]):
    sum_slice = ap
    for len_slice, aq in enumerate(A[p+1:p+3], 2):
      sum_slice += aq
      if (avg := sum_slice / len_slice) < min_avg:
        min_avg, ret = avg, p

  return ret


def solution3(A):
  pref = list(accumulate(A, initial=0))

  min_avg, ret = pref[2] / 2, 0
  p, q = 0, 1
  slice_size = 2
  while q < len(A):
    if (avg := (pref[q+1]-pref[p]) / slice_size) < min_avg:
      min_avg, ret = avg, p

    if slice_size == 2:
      q += 1
      slice_size += 1
    else:
      p += 1
      slice_size -= 1

  return ret


def slow_solution(A):
  N = len(A)
  pref = list(accumulate(A, initial=0))

  min_avg, ret = pref[2] / 2, 0
  for p in range(N-1):
    for q in range(p+1, N):
      if (avg := (pref[q+1]-pref[p]) / (q-p+1)) < min_avg:
        min_avg, ret = avg, p

  return ret


if __name__ == '__main__':
  from random import randrange

  solutions = [(fname, f) for fname, f in globals().items()
               if 'solution' in fname]

  cases = [
      ([4, 2, 2, 5, 1, 5, 8],),
      ([0, 0],),
  ]
  cases.extend([
      ([randrange(-4, 4) for _ in range(randrange(2, 6))],)
      for _ in range(6)
  ])
  for c in cases:
    results = {fname: f(*c) for fname, f in solutions}
    print(f'\n{c = }')
    print(f'{results = }')

  cases2 = [
      ([randrange(-10000, 10001) for _ in range(randrange(2, 100))],)
      for _ in range(10000)
  ]
  for c in cases2:
    results = {fname: f(*c) for fname, f in solutions}
    if len(set(results.values())) != 1:
      print(f'\n{c = }')
