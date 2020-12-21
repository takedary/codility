def solution(N):
  i, counter = 1, 0
  while i * i <= N:
    if N % i == 0:
      counter += 2
    i += 1
  i -= 1
  if i * i == N:
    print('pow')
    counter -= 1
  return counter


if __name__ == '__main__':
  cases = [24, 1, 2, 3, 4, 5, 6, 8, 9, 11, 12, 720]
  for c in cases:
    print(c, solution(c))
