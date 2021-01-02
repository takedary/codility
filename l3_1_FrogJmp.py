def solution(X, Y, D):
  return -(-(Y-X) // D)


if __name__ == '__main__':
  cases = [
      (10, 85, 30),
      (10, 85, 26),
      (10, 85, 25),
      (10, 85, 24),
  ]
  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
