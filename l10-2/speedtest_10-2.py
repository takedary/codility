import math
import random
import timeit

import solutions


def rand_unif(left, right):
  return left + (right-left)*random.random()

def rand_logunif(left, right):
  return pow(10, rand_unif(math.log10(left), math.log10(right)))

def generate_peaks(p, N, r):
  max_gap = r * (N - p)
  while p < N - 1:
    yield p
    p += int(rand_logunif(2, 2 + max_gap))


SETUP = '''
cases = []
for _ in range(10000):
  N = max(int(pow(10, 5*random.random())), 3)
  p = int(rand_logunif(1, N-2))
  peaks = list(generate_peaks(p, N, random.random()))
  cases.append((peaks, N))
'''

TEST = '''
for c in cases:
  solutions.peaks2flags(c[0], c[1], {search}, {check})
'''

if __name__ == '__main__':
  repeat = 5
  for search in ['linear', 'binary']:
    for check in ['naive', 'next']:
      test = TEST.format(search=search.join('""'), check=check.join('""'))
      tt = timeit.repeat(stmt=test, setup=SETUP, globals=globals(),
                         repeat=5, number=1)
      print('{} search + {} check: {}'.format(
          search, check, ', '.join(['{:.5f}'.format(t) for t in sorted(tt)])))
