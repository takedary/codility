def solution(A, B):
  if not A:
    return 0

  count = 0
  end = A[0] - 1
  for l, r in zip(A, B):
    if end < l:
      count += 1
      end = r
  return count


if __name__ == '__main__':
  cases = [
      ([1, 2, 3], [4, 5, 6]),
      ([3, 1, 2, 7], [4, 5, 6, 8]),
      ([2, 4, 1], [3, 5, 6]),
      ([2, 3, 1], [3, 5, 6]),
  ]
  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
