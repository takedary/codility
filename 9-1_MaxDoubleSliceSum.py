import random
import sys


def solution(A):
  """
  s1[n]: max sum of double slice such that Z < n
  s2[n]: max sum of double slice such that Z = n
  y[n]:  Y in s2[n]
  s3[n]: max sum of single slice such that Z = n
  """
  s1 = s2 = 0
  y = 1
  s3 = max(0, A[1])
  for i in range(3, len(A)):
    s1 = max(s1, s2)
    s2, y = sorted([(s2 + A[i-1], y), (0, i-1), (s3, i-1)])[-1]
    s3 = max(s3 + A[i-1], A[i-1], 0)
  return max(s1, s2)


def slow_solution(A):
  N = len(A)
  maxs = -sys.maxsize
  for x in range(N-2):
    for y in range(x+1, N-1):
      for z in range(y+1, N):
        s = sum(A[x+1:y]) + sum(A[y+1:z])
        maxs = max(s, maxs)
  return maxs


if __name__ == '__main__':
  #cases = [
  #    [3, 2, 6, -1, 4, 5, -1, 2],
  #    [3, 2, -6, -1, 4, 5, -1],
  #    [-3, -2, -6, -1, -4, 5, -1],
  #    [random.randrange(-10, 10) for _ in range(6)],
  #    [random.randrange(-10, 10) for _ in range(6)],
  #    [random.randrange(-10, 10) for _ in range(6)]
  #]
  #cases = [[-1, -6, 7, -4, 2, -7]]
  #for c in cases:
  #  print(c)
  #  print('answer:', solution(c), 'slow:', slow_solution(c))
  cases = [[random.randrange(-1000, 1000) for i in range(70)]
           for j in range(100)]
  for c in cases:
    if solution(c) != slow_solution(c):
      print(c, 'answer:', solution(c), 'slow:', slow_solution(c))