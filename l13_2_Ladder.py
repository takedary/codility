def solution(A, B):
  mask = (1 << max(B)) - 1

  nways = [1, 1]
  for _ in range(2, max(A) + 1):
    nways.append((nways[-2] + nways[-1]) & mask)

  return [nways[a] & ((1 << b) - 1) for a, b in zip(A, B)]


if __name__ == '__main__':
  cases = [
      ([1, 2, 3, 4, 5, 6, 15], [3, 2, 1, 3, 2, 1, 20]),
      ([4, 4, 5, 5, 1], [3, 2, 4, 3, 1]),
  ]
  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
