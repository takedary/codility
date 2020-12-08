import random
import sys


def solution(A):
  pref_maxa = []
  maxa = -sys.maxsize
  for a in reversed(A):
    if a > maxa:
      maxa = a
    pref_maxa.append(maxa)
  pref_maxa.reverse()

  mina = sys.maxsize
  max_profit = -sys.maxsize
  for i, a in enumerate(A):
    if a < mina:
      mina = a
    if pref_maxa[i] - mina > max_profit:
      max_profit = pref_maxa[i] - mina
  return max(0, max_profit)


if __name__ == '__main__':
  cases = [[random.randrange(-10, 10) for i in range(5)]
           for j in range(10)]
  for c in cases:
    print(c)
    print(solution(c))
    #if solution(c) != slow_solution(c):
    #  print(c, 'answer:', solution(c), 'slow:', slow_solution(c))
