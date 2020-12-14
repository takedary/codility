import math


def solution(N):
  a = int(math.sqrt(N))
  for i in range(a, 0, -1):
    if N % i == 0:
      return 2 * (i + int(N/i))
