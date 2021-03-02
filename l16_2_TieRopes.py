def solution(K, A):
  length = 0
  count = 0
  for a in A:
    length += a
    if length >= K:
      count += 1
      length = 0
  return count


if __name__ == '__main__':
  from random import randrange

  cases = []
  for _ in range(5):
    cases.append((
        randrange(1, 10),
        [randrange(1, 10) for _ in range(randrange(1, 5))]
    ))
  
  for c in cases:
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
