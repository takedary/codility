def solution(A, K):
  if not A or not K:
    return A
  K %= len(A)
  return A[-K:] + A[:-K]


if __name__ == '__main__':
  cases = [
      ([], 0),
      ([], 1),
      ([1], 0),
      ([1], 1),
      ([1], 2),
      ([1, 2, 3, 4], 0),
      ([1, 2, 3, 4], 1),
      ([1, 2, 3, 4], 2),
      ([1, 2, 3, 4], 3),
      ([1, 2, 3, 4], 4),
      ([1, 2, 3, 4], 5),
  ]
  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
