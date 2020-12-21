from collections import Counter


def solution(A):
  n = len(A)
  max_a = max(A)
  d = [n] * (max_a + 1)
  c = Counter(A)
  for a in c:
    for i in range(1, max_a//a + 1):
      d[i * a] -= c[a]
  return [d[a] for a in A]

def slow_solution(A):
  ret = [0] * len(A)
  for i, a in enumerate(A):
    for aa in A:
      if a % aa != 0:
        ret[i] += 1
  return ret


TEST = '''
for c in cases:
  {solution}(c)
'''


if __name__ == '__main__':
  import random
  import timeit

  cases = [[3, 1, 2, 3, 6]]
  for _ in range(100):
    N = random.randrange(1, 500+1)
    cases.append([random.randrange(1, 2*N+1) for _ in range(N)])

  for c in [case for case in cases if len(case) < 10]:
    print('\n', c)
    print('slow:', slow_solution(c), sep='\t')
    print('mine:', solution(c), sep='\t')

  for c in cases:
    if solution(c) != slow_solution(c):
      print('\nGot wrong answer on', c)

  print('\ntimeit')
  print('slow:',
        timeit.repeat(TEST.format(solution='slow_solution'),
                      globals=globals(), repeat=5, number=1),
        sep='\t'
  )
  print('mine:',
        timeit.repeat(TEST.format(solution='solution'),
                      globals=globals(), repeat=5, number=1),
        sep='\t'
  )
