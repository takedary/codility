from collections import defaultdict


def solution(N, A):
  max_count = 0
  sector_counter = defaultdict(int)
  sector_max = 0
  for a in A:
    if a <= N:
      sector_counter[a] += 1
      sector_max = max(sector_max, sector_counter[a])
    elif sector_counter:
      max_count += sector_max
      sector_counter.clear()
      sector_max = 0

  return [max_count + sector_counter[k] for k in range(1, N+1)]


def another_solution(N, A):
  max_count = 0
  sector_counter = defaultdict(int)
  for a in A:
    if a <= N:
      sector_counter[a] += 1
    elif sector_counter:
      max_count += max(sector_counter.values())
      sector_counter.clear()

  return [max_count + sector_counter[k] for k in range(1, N+1)]


def another_solution_2(N, A):
  last_max, current_max = 0, 0
  counter = defaultdict(int)
  for a in A:
    if a <= N:
      counter[a] = max(counter[a], last_max) + 1
      current_max = max(current_max, counter[a])
    else:
      last_max = current_max

  return [max(last_max, counter[k]) for k in range(1, N+1)]


def slow_solution(N, A):
  counter = {i: 0 for i in range(1, N+1)}
  for a in A:
    if a <= N:
      counter[a] += 1
    else:
      max_count = max(counter.values())
      for k in counter.keys():
        counter[k] = max_count
  return list(counter.values())


if __name__ == '__main__':
  from random import randrange

  cases = [
      (5, [3, 4, 4, 6, 1, 4, 4]),
      (5, [3, 4, 4, 6, 1, 1, 1, 6, 3]),
      (5, [6, 6]),
  ]
  for _ in range(6):
    N = randrange(1, 4)
    cases.append((N, [randrange(1, N+2) for _ in range(randrange(1, 10))]))

  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
    print(f'{another_solution(*c) = }')
    print(f'{another_solution_2(*c) = }')
    print(f'{slow_solution(*c) = }')
