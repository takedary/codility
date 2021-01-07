from itertools import accumulate


def solution(S, P, Q):
  nucleotides = 'ACGT'
  counts = [list(accumulate((s == n for s in S), initial=0)) # for python < 3.8, [0] + list(accumulate(int(s == n) for s in S))
            for n in nucleotides]

  def min_ifac(p, q):
    for ifac, (n, count) in enumerate(zip(nucleotides, counts), 1):
      if count[q+1] - count[p] > 0:
        return ifac

  return [min_ifac(p, q) for p, q in zip(P, Q)]


if __name__ == '__main__':
  from random import choices, randrange

  cases = [
      ('CAGCCTA', [2, 5, 0], [4, 5, 6]),
      ('C', [0], [0]),
  ]
  for _ in range(6):
    N = randrange(1, 9)
    S = choices('ACGT', k=N)
    P = [randrange(N) for _ in range(2)]
    Q = [randrange(p, N) for p in P]
    cases.append((S, P, Q))

  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
