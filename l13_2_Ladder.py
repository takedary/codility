def solution(A, B):
  mask = 2 ** max(B) - 1
  ways = [1, 1]
  for _ in range(2, max(A) + 1):
    ways.append((ways[-2] + ways[-1]) & mask)
  return [ways[a] % 2**b for a, b in zip(A, B)]


if __name__ == '__main__':
  cases = [
      ([1, 2, 3, 4, 5, 6, 15], [3, 2, 1, 3, 2, 1, 20]),
  ]
  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
