def solution(A, B):
  num_up_fishes_alive = 0
  down_fishes_alive = []
  for size, direction in zip(A, B):
    if direction == 0:
      while down_fishes_alive and down_fishes_alive[-1] < size:
        down_fishes_alive.pop()
      if not down_fishes_alive:
        num_up_fishes_alive += 1
    else:
      down_fishes_alive.append(size)
  return num_up_fishes_alive + len(down_fishes_alive)


if __name__ == '__main__':
  cases = [
      ([8, 5, 2, 0, 1], [1, 0, 1, 0, 1]),
      ([1, 0, 2, 5, 8], [1, 0, 1, 0, 1]),
      ([4, 3, 2, 1, 5], [1, 0, 1, 0, 1]),
      ([1, 5, 2, 4, 3], [1, 0, 1, 0, 1]),
      ([5, 2, 1], [1, 0, 0]),
      ([5, 2, 1], [0, 1, 1]),
      ([1], [0]),
      ([1], [1]),
  ]
  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
