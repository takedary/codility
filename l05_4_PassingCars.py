def solution(A):
  cars_east = passing_cars = 0
  for a in A:
    if a == 0:
      cars_east += 1
    else:
      passing_cars += cars_east
      if passing_cars > 10**9:
        return -1
  return passing_cars


if __name__ == '__main__':
  cases = [
      ([0, 0],),
      ([0, 1],),
      ([1, 0],),
      ([1, 1],),
      ([0, 1, 0, 1, 1],),
  ]
  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
