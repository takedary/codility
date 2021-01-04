def solution(X, A):
  places = set(range(1, X+1))
  for t, a in enumerate(A):
    places.discard(a)
    if not places:
      return t
  return -1


def another_solution(X, A):
  leaves = set()
  for t, a in enumerate(A):
    if a not in leaves:
      covered_time = t
      leaves.add(a)

  if len(leaves) != X:
    return -1
  return covered_time


if __name__ == '__main__':
  cases = [
      (5, [1, 3, 1, 4, 2, 3, 5, 4]),
      (1, [1]),
      (2, [1]),
      (2, [2]),
      (2, [1, 2]),
      (2, [1, 1, 1]),
      (2, [1, 1, 2]),
      (2, [2, 1, 2]),
  ]
  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
    print(f'{another_solution(*c) = }')
