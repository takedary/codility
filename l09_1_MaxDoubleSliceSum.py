import random
import sys


def solution(A):
  """
  sd[z]: max sum of double slice (X, Y, Z) such that Z = z
  ss[z]: max sum of single slice (X, Y) such that Y = z
  """
  sd = 0
  ss = max(0, A[1])
  max_sd = 0
  for z in range(3, len(A)):
    sd = max(sd + A[z-1], ss)
    max_sd = max(max_sd, sd)
    ss = max(ss + A[z-1], A[z-1], 0)
  return max_sd


def slow_solution(A):
  N = len(A)
  maxsum = 0
  for x in range(N-2):
    for z in range(x+2, N):
      maxsum = max(maxsum, sum(A[x+1:z]) - min(A[x+1:z]))
  return maxsum


if __name__ == '__main__':
  cases = [[random.randrange(-10, 10) for i in range(5)] for j in range(10)]
  for c in cases:
    print(c)
    print(solution(c))
    #if solution(c) != slow_solution(c):
    #  print(c, 'answer:', solution(c), 'slow:', slow_solution(c))
