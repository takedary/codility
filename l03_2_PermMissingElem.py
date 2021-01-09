def solution(A):
  return (set(range(1, len(A)+2)) - set(A)).pop()


if __name__ == '__main__':
  cases = [
      ([],),
      ([2, 3, 1, 5],),
      ([2],),
      ([1],),
  ]
  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
