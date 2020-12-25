def solution(A, B):
  A.sort(reverse=True)
  B.sort(reverse=True)

  counter = 0
  for a in reversed(A):
    while B and B[-1] <= a:
      _ = B.pop()
    if not B:
      break
    counter += 1
    _ = B.pop()

  return counter


if __name__ == '__main__':
  from random import randrange

  cases = [
      ([5, 9, 2], [8, 4, 1]),
      ([2, 6, 3], [8, 4, 1]),
  ]
  for _ in range(5):
    N = randrange(1, 5)
    cases.append((
        [randrange(5) for _ in range(N)], [randrange(5) for _ in range(N)]
    ))

  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
