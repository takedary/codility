def solution(N, M):
  def gcd(a, b):
    if a % b == 0:
      return b
    return gcd(b, a % b)

  return N // gcd(N, M)

def slow_solution(N, M):
  counter = 0
  w = [True] * N
  n = 0
  while w[n]:
    w[n] = False
    counter += 1
    n = (n + M) % N
  return counter


if __name__ == '__main__':
  from random import randrange


  cases = [
      (10, 4),
      (4, 10),
      (10, 3),
      (3, 10),
      (947853, 4453),
      ((3**9) * (2**14), (2**14) * (2**14)),
  ]
  for c in cases:
    print('\n', c)
    print(f'{slow_solution(*c)=}')
    print(f'{solution(*c)=}')


  # collectness test
  cases = []
  for _ in range(600):
    N = randrange(1, 1000)
    M = randrange(1, 1000)
    cases.append((N, M))

  for c in cases:
    if solution(*c) == slow_solution(*c):
      continue
    print(f'{solution(*c)=}')
    print(f'{slow_solution(*c)=}')
