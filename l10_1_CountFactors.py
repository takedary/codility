from math import sqrt


def solution(N):
  n_factors = 0
  for i in range(1, int(sqrt(N)) + 1):
    if N % i == 0:
      n_factors += 2
  if i * i == N:
    n_factors -= 1
  return n_factors


if __name__ == '__main__':
  cases = [(24,), (720,), (2147483646,), (2147483647,)]
  for i in range(1, 14):
    cases.append((i,))
  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
