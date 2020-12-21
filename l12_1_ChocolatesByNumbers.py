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
  cases = [
      (10, 4),
      (10, 3),
      (947853, 4453),
      ((3**9) * (2**14), (2**14) * (2**14)),
  ]
  for c in cases:
    print('\n', c)
    print(f'{slow_solution(*c)=}')
    print(f'{solution(*c)=}')
