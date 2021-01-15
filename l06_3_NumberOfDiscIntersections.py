def solution(A):
  if not A:
    return 0

  ends = []
  for i, a in enumerate(A):
    ends.append((i - a, 'l'))
    ends.append((i + a, 'r'))
  ends.sort(key=lambda x: x[1])
  ends.sort(key=lambda x: x[0])

  disks = 0
  intersections = 0
  for _, lr in ends:
    if lr == 'l':
      intersections += disks
      if intersections > 10**7:
        return -1
      disks += 1
    else:
      disks -= 1
  return intersections


def better_solution(A):
  """
  O(N)
  """
  if not A:
    return 0

  N = len(A)
  lefts, rights = [0] * N, [0] * N
  for i, a in enumerate(A):
    lefts[max(0, i - a)] += 1
    rights[min(i + a, N - 1)] += 1

  disks = 0
  intersections = 0
  for l, r in zip(lefts, rights):
    intersections += l * (disks + (disks+l-1)) // 2
    if intersections > 10**7:
      return -1
    disks += l - r
  return intersections


if __name__ == '__main__':
  cases = [
      ([1, 5, 2, 1, 4, 0],),
      ([1, 1, 1, 1],),
  ]
  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
    print(f'{better_solution(*c) = }')
