def gen_fibo(m):
  """
  return fibonacci seq while <= m, ommiting first two numbers
  """
  a, b = 1, 1
  while b <= m:
    yield b
    a, b = b, a + b

def solution(A):
  if not A:
    return 1

  N = len(A)
  if N + 1 in set(gen_fibo(N + 1)):
    return 1

  d = {-1: 0}
  def min_jumps(i, ind):
    def points_to_check(j):
      for n in reversed(list(gen_fibo(N + 1))):
        k = j - n
        if k < -1:
          continue
        if k == -1 or A[k]:
          if d.get(k, 0) != -1:
            yield k

    ind += ' ' * 4
    print(ind, '[entered]', f'{i = }')
    try:
      print(ind, '[exit]', 'd[{}] = {}'.format(i, d[i]), '(known)')
      return d[i]
    except KeyError:
      pass

    print(ind, '{} -> {}'.format(i, list(points_to_check(i))))
    jumps = []
    for p in points_to_check(i):
      j = min_jumps(p, ind)
      if j != -1:
        jumps.append(j)
      if j == 0:
        break
    print(ind, f'{jumps = }')

    if jumps:
      d[i] = min(jumps) + 1
    else:
      d[i] = -1
    print(ind, '[exit]', 'd[{}] = {}'.format(i, d[i]))
    return d[i]

  ret = min_jumps(N, '')
  print(d)
  return ret

if __name__ == '__main__':
  cases = [
      ([4, 7, 8, 13], 15),
      ([3, 4, 6], 11),
  ]
  for c in cases:
    cc = [0] * c[1]
    for i in c[0]:
      cc[i] = 1
    c = (cc,)
    print(f'\n{c = }')
    print(f'{solution(*c) = }')
