def solution(M, A):
  N = len(A)

  l = r = 0
  count = 0
  d = {}
  while r < N:
    print(l, r)
    print(d)
    ar = A[r]
    if ar not in d:
      d[ar] = r
      r += 1
    else:
      dar = d[ar]
      # r-l + r-l-1 + r-l-2 + ... + r-d[ar]
      count += (2 * r - l - dar) * (dar - l + 1) // 2
      for i in range(l, dar + 1):
        del d[A[i]]
      l = dar + 1
  count += (N - l) * (N - l + 1) // 2

  return count


if __name__ == '__main__':
  cases = [
      (None, [4, 2, 9, 8, 0, 7, 3, 8, 7, 4]),
      (None, [3, 4, 5, 5, 2]),
  ]
  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
