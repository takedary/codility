import random
import sys


def solution(A):
  m, maxm = -sys.maxsize, -sys.maxsize
  for a in A:
    m = max(m + a, a)
    maxm = max(m, maxm)
  return maxm


if __name__ == '__main__':
  cases = [
      [1, 3, -5, 3],
      [1],
      [-2, -3, -3]
  ]
  for _ in range(4):
    cases.append([random.randrange(-10, 10) for i in range(5)])

  for c in cases:
    print(c)
    print(solution(c))
