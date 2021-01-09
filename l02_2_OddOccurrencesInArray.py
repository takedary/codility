from collections import Counter


def solution(A):
  s = set()
  for a in A:
    try:
      s.remove(a)
    except KeyError:
      s.add(a)
  return s.pop()


def shorter_solution(A):
  for a, count in Counter(A).items():
    if count % 2:
      return a


if __name__ == '__main__':
  from random import choice, randrange

  cases = [
      ([1],),
      ([1, 1, 1],),
      ([1, 2, 1],),
  ]
  for _ in range(6):
    c = []
    for _ in range(2):
      a = randrange(1, 10)
      for _ in range(choice([2, 4])):
        c.append(a)
    a = randrange(1, 10)
    for _ in range(choice([1, 3])):
      c.append(a)
    cases.append((c,))

  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
    print(f'{shorter_solution(*c) = }')
