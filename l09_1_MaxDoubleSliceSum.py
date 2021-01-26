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


def another_solution(A):
  """
  ss_l[y]: max sum of single slice (X, Y) such that Y = y
  ss_r[y]: max sum of single slice (Y, Z) such that Y = y
  """
  N = len(A)
  A = list(A)
  A[0] = A[-1] = -sys.maxsize

  ss_l = [0] * N
  for y in range(1, N-1):
    ss_l[y] = max(ss_l[y-1] + A[y-1], A[y-1], 0)

  ss_r = [0] * N
  for y in reversed(range(1, N-1)):
    ss_r[y] = max(ss_r[y+1] + A[y+1], A[y+1], 0)

  return max(l + r for l, r in zip(ss_l, ss_r))


def slow_solution(A):
  N = len(A)
  maxsum = 0
  for x in range(N-2):
    for z in range(x+2, N):
      maxsum = max(maxsum, sum(A[x+1:z]) - min(A[x+1:z]))
  return maxsum


if __name__ == '__main__':
  from random import randrange

  cases = []
  for _ in range(6):
    N = randrange(3, 8)
    c = ([randrange(-10, 10) for _ in range(N)],)
    cases.append(c)
  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
    print(f'{another_solution(*c) = }')
    print(f'{slow_solution(*c) = }')

  # collectness test
  cases = []
  for _ in range(600):
    N = randrange(3, 100)
    c = ([randrange(-N, N) for _ in range(N)],)
    cases.append(c)
  for c in cases:
    if not solution(*c) == another_solution(*c) == slow_solution(*c):
      print(f'\n{c = }')
