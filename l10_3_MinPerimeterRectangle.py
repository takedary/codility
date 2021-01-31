from math import sqrt


def solution(N):
  s = int(sqrt(N))
  for a in range(s, 0, -1):
    if N % a == 0:
      return 2 * (a + N//a)


if __name__ == '__main__':
  cases = [(1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,), (30,)]
  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
