def solution(A, B, K):
  return B//K - A//K + (A%K == 0)


def another_solution(A, B, K):
  return B//K + (-A//K) + 1


if __name__ == '__main__':
  from random import randrange

  cases = [
      (0, 0, 3),
      (0, 1, 3),
      (0, 2, 3),
      (0, 3, 3),
      (0, 4, 3),
      (5, 5, 3),
      (5, 6, 3),
      (5, 7, 3),
      (5, 8, 3),
      (5, 9, 3),
      (6, 10, 13),
      (6, 9, 5),
  ]
  for _ in range(6):
    A = randrange(0, 7)
    B = randrange(A, A + 10)
    K = randrange(1, 20)
    cases.append((A, B, K))

  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
    print(f'{another_solution(*c) = }')
