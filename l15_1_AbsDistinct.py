def solution(A):
  return len(set(abs(a) for a in A))


if __name__ == '__main__':
  cases = [
      ([-5, -3, -1, 0, 3, 6],),
      ([-5, -1, -1, 0, 0, 6],),
      ([-5, -3, -3, 3, 3, 6],),
  ]
  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
